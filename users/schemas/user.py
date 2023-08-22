from django import forms

class signupSchema(forms.Form):
    username = forms.CharField(max_length=30)
    _password = forms.CharField(widget=forms.PasswordInput)
    role = forms.CharField(required=False,initial="emp")

class loginSchema(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    