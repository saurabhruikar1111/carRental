from django.shortcuts import render
from . schemas.user import signupSchema,loginSchema
from django.http import HttpResponse ,HttpResponseBadRequest
from . models import UserAuthonticationModel
import json

def signup(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        form = signupSchema(data=data)
        if form.is_valid():
            if UserAuthonticationModel.objects.filter(username=data["username"]).first():
                return HttpResponse(f"please enter unique username {data['username']} already exists")
            new_user = UserAuthonticationModel(**data)
            new_user.set_password(data["password"])
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
            
            if not new_user:
                return HttpResponseBadRequest("username does not exisists")
            print(data["password"])
            if not new_user.check_password(data["password"]):
                return HttpResponseBadRequest("Incorrect credentials, please try again")
            return HttpResponse("user login successfully")
        return HttpResponseBadRequest("Invalid input to form")
        
    return HttpResponseBadRequest("Method only accepts post method")
        

