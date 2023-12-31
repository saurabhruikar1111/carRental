from django.urls import path
from . import views
from .admin_functions import handleEmployees

urlpatterns = [
    path("signup",views.signup,name="user-signup"),
    path("login",views.login),
    path("check_username_exists",views.check_username_exists,name="user-check-username-exists"),
    path("protected",views.protected_method,name="user-protected"),
    path("create_employee", handleEmployees.create_employee)
]