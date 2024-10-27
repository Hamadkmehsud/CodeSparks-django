from django import forms
from django.contrib.auth.hashers import make_password

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput for security
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    image = forms.ImageField(required=False)  # Make it optional

