// Code taken from Code Institute lesson
$(function(){
    // Checking if poll box is checked
    if(!$('#id_is_a_poll').is('checked')){
        $('#poll_form').hide()
    }
    $('#id_is_a_poll').click(function(el){
        // Toggling the display of the poll form
        var poll_form = $('#poll_form');
        if(poll_form.is(':visible')){
            poll_form.hide()
        } else{
            poll_form.show()
        }
    })
});