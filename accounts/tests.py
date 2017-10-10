from __future__ import unicode_literals
from django.test import TestCase
from .forms import UserRegistrationForm, UserSubscriptionForm
from django import forms
from django.conf import settings


class CustomerUserTest(TestCase):

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'logmein',
            'password2': 'logmein',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_password_not_matching(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'logmein',
            'password2': 'logemin',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, 'Passwords do not match', form.full_clean())

    def test_registration_form_fails_with_no_email(self):
        form = UserRegistrationForm({
            'password1': 'logmein',
            'password2': 'logmein',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, 'Please enter your email address', form.full_clean())

    def test_subscription_form(self):
        form = UserSubscriptionForm({
            'email': 'test@test.com',
            'password1': 'logmein',
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2030,
            'stripe_id': settings.STRIPE_SECRET
        })
        self.assertTrue(form.is_valid())
