from django.shortcuts import render
from . schemas.user import signupSchema,loginSchema
from django.http import HttpResponse ,HttpResponseBadRequest,JsonResponse
from . models import UserAuthonticationModel,EmployeeLoginDetails
import json
from .utils import session_data
from datetime import datetime

def signup(request):
    if request.method == "GET":
        return render(request,"users/signupPage.html")
    
    if request.method == "POST":
        # data = json.loads(request.body.decode("utf-8"))
        data = {"username":request.POST.get("username"),
                "_password":request.POST.get("password"),
                "role":request.POST.get("role","emp")
                }
        form = signupSchema(data=data)
        if form.is_valid():
            if UserAuthonticationModel.objects.filter(username=data["username"]).first():
                return HttpResponse(f"please enter unique username {data['username']} already exists")
            new_user = UserAuthonticationModel(**data)
            new_user.save()
            return HttpResponse("valid form was submitted")
        return HttpResponse("form was not valid")
    return HttpResponseBadRequest("Method only accepts post method")

def login(request):
    
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        form = loginSchema(data=data)

        if form.is_valid():
            new_user = UserAuthonticationModel.objects.filter(username=data["username"]).first()
            print(data)
            if not new_user:
                return HttpResponseBadRequest("username does not exisists")
            
            if not new_user.verify_password(data["password"]):
                return HttpResponseBadRequest("Incorrect Password, please try again")
            
            # token verification
            if data.get("special_token",""):
                employee_model = new_user.employee_details.first()
                if not employee_model.verify_token(data["special_token"]):
                    return HttpResponseBadRequest("Incorrect Token, try again")
                print(datetime.now(),employee_model.datetime_employee_registered)
                if not employee_model.is_within_days_from_current_time(hours=7):
                    return HttpResponse("Token expire please contact the admin for renewing tokens")


            session_data_obj = session_data(**new_user.get_session_data())
            print(new_user.role)
            request.session["session_data"] = session_data_obj.serialise()
            return HttpResponse(f"user login successfully new session started user: {data.get('role','reg')}")
        return HttpResponseBadRequest("Invalid input to form")
        
    return HttpResponseBadRequest("Method only accepts post method")


def check_username_exists(request):
    username = request.GET.get('username', None)
    
    if username:
        user_exists = UserAuthonticationModel.objects.filter(username=username).exists()
        if user_exists:
            response = "true"
        else:
            response = "false"
    else:
        response = "error"

    return JsonResponse(response, safe=False)

def protected_method(request):
    if "session_data" in request.session:
        return HttpResponse("you are logged in, Welcome")
    return HttpResponse("please login first")