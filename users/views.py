from django.shortcuts import render
from . schemas.user import signupSchema,loginSchema
from django.http import HttpResponse ,HttpResponseBadRequest,JsonResponse
from . models import UserAuthonticationModel
import json
from django.contrib import sessions

def signup(request):
    if request.method == "GET":
        return render(request,"users/signupPage.html")
    
    if request.method == "POST":
        # data = json.loads(request.body.decode("utf-8"))
        data = {"username":request.POST.get("username"),
                "password":request.POST.get("password"),
                "role":request.POST.get("role","emp")
                }
        print(data)
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
            new_user = UserAuthonticationModel.objects.filter(username=data["username"]).values("username","password").first()
            
            if not new_user:
                return HttpResponseBadRequest("username does not exisists")
            
            if not new_user.check_password(data["password"]):
                return HttpResponseBadRequest("Incorrect credentials, please try again")
            request.session["username"] = data["username"]
            return HttpResponse("user login successfully new session started")
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
    if "username" in request.session:
        return HttpResponse("you are logged in, Welcome")
    return HttpResponse("please login first")