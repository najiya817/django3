from django import forms

class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.IntegerField()
    confirm_pass=forms.IntegerField

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.IntegerField()
