from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.

class UserAuthonticationModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=5,default="emp")

    def set_password(self,raw_password):
        self.password = make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(raw_password,self.password)


