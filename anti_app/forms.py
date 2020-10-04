from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()

    address = forms.CharField()
    city = forms.CharField()
    zip_code = forms.IntegerField()

    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']