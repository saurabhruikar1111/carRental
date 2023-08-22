from django.db import models
from django.contrib.auth.hashers import make_password,check_password
#from django.utils import timezone
from datetime import datetime,timedelta
# Create your models here.

class UserAuthonticationModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    _password = models.CharField(max_length=150)
    role = models.CharField(max_length=5,default="emp")
    datetime_user_registered = models.DateTimeField(default=datetime.now())
    datetime_user_updated = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=True) 

    # constructor for hashing _password
    def __init__(self, *args, **kwargs):
        raw__password = kwargs.pop('_password', None)  # Remove '_password' from kwargs
        super(UserAuthonticationModel, self).__init__(*args, **kwargs)  # Call parent constructor
        
        if raw__password:
            self._password = make_password(raw__password)  # Hash the _password if provided

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,raw_password):
        self._password = make_password(raw_password)

    def verify_password(self,raw_password):
        return check_password(raw_password,self._password)
    
    def get_session_data(self):
        dic = {"username":self.username,
               "id":self.id,
               "role":self.role
               }
        return dic

class EmployeeLoginDetails(models.Model):
    special_token = models.CharField(max_length=150,null=True)
    datetime_employee_registered = models.DateTimeField(default=datetime.now())

    # constructor for hashing token
    def __init__(self, *args, **kwargs):
        special_token = kwargs.pop('special_token', None)  # Remove '_password' from kwargs
        super(EmployeeLoginDetails, self).__init__(*args, **kwargs)  # Call parent constructor

        if special_token:
            self.special_token = make_password(special_token)  # Hash the _password if provided

    @property
    def token(self):
        return self.special_token
    
    @token.setter
    def password(self,raw_password):
        self.special_token = make_password(raw_password)


