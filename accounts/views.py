from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm, UserSubscriptionForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from models import User
import json
import stripe
import arrow
stripe.api_key = settings.STRIPE_SECRET


# Code taken from Code Institute Lesson
class UserView(APIView):

    permission_classes = ()

    def post(self,request):
        """Creating a separate User for editing API data"""
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            user = User.objects.create(username=data["username"])
            user.set_password(data["password"])
            user.save()
            return Response(data, status=status.HTTP_201_CREATED)


# Code edited from Code Institute Lesson
def register(request):
    """Submitting regular User form if it is valid"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'register.html', args)


@login_required(login_url='/login/')
def subscribe(request):
    """Setting up user subscription"""
    if request.method == 'POST':
        form = UserSubscriptionForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                    plan='REG_MONTHLY'
                )
                if customer:
                    user = request.user
                    user.stripe_id = customer.stripe_id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()
                    return redirect(reverse('profile'))
                else:
                    messages.error(request, "We were unable to take payment from the card provided")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
                form.add_error(None, "Ooops! Details entered are incorrect, please check them!")
    else:
        form = UserSubscriptionForm()
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'stripe.html', args)


# Code taken from Code Institute Lesson
@login_required(login_url='/login/')
def cancel_subscription(request):
    """Cancelling user subscription at the end of 4 weeks paid for"""
    try:
        customer = stripe.Customer.retrieve(request.user.stripe_id)
        customer.cancel_subscription(at_period_end=True)
    except Exception, e:
        messages.error(request, e)
    return redirect('profile')


# Code taken from Code Institute Lesson
@csrf_exempt
def subscriptions_webhook(request):
    """Checking payment / renewal successful and updating subscription expiry date"""
    event_json = json.loads(request.body)
    try:
        event = stripe.Event.retrieve(event_json['object']['id'])
        cust = event_json['object']['customer']
        paid = event_json['object']['paid']
        user = User.objects.get(stripe_id=cust)
        if user and paid:
            user.subscription_end = arrow.now().replace(weeks=+4).datetime
            user.save()
    except stripe.InvalidRequestError, e:
        return HttpResponse(status=404)
    return HttpResponse(status=200)


@login_required(login_url='/login/')
def profile(request):
    """Getting a users profile"""
    return render(request, 'profile.html')


# Code taken from Code Institute Lesson
def login(request):
    """Log in form"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
    else:
        form = UserLoginForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    """Logs user out"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
