from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseServerError
#from ..utils import session_data
from faker import Faker
from ..models import UserAuthonticationModel,EmployeeLoginDetails
from django.db import transaction

def create_employee(request):
    if "session_data" not in request.session:
        return HttpResponseBadRequest("Please login first, before accessing these service")
    if request.session.get("session_data").get("role","adm") != "adm":
        return HttpResponseForbidden("You are not authorised for these service")
    
    fake = Faker()
    username = fake.user_name()
    password = "saurabh12345"
    special_token = "xyz"

    employee = UserAuthonticationModel(username=username,password=password)
    
    try:
        with transaction.atomic():
            employee.save()
            employeeCredentials = EmployeeLoginDetails(special_token=special_token,user=employee)
            employeeCredentials.save()
    except Exception as e:
        transaction.set_rollback(True)
        return HttpResponseServerError("Something went wrong please try again later")
    
    
    message = f"""
    hello,
    username: {username},
    password: {password},
    special_token: {special_token}

    Please use above credentials to login within next 24 hours. 
    After 24 hours above credentials will not work

    Thanks and Regards,
    admin carRentals.com 
    """
    
    subject = 'Your login credentials'
    #message = 'This is a test email sent from Django.'
    from_email = 'saurabh@saurabh.com'
    recipient_list = ['kamille78@ethereal.email']
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Mail sent successfully")