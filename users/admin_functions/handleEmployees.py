from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest
from ..utils import session_data


def create_employee(request):
    if "session_data" not in request.session:
        return HttpResponseBadRequest("Please login first, before accessing these service")
    if request.session.get("session_data").get("role","adm") != "adm":
        return HttpResponseForbidden("You are not authorised for these service")
    
    #fake = Faker()

    username = fake.user_name()
    password = "saurabh12345"
    special_token = "xyz"
    
    subject = 'Hello from Django'
    message = 'This is a test email sent from Django.'
    from_email = 'saurabh@saurabh.com'
    recipient_list = ['kamille78@ethereal.email']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Mail sent successfully")