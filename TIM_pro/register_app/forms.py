from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     # we're inheriting from the forms, to change/overwrite the properties of parent , we write meta
        model = User # Currently the in built form only has the username and pass fields ,this step will help us add other fields also
        fields = ['username', 'email', 'password1','password2']  # the order in which the field will show up

