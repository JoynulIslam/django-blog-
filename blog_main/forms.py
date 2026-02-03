from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Invalid credentials! Please check your username and password.",
        'inactive': "This account is inactive.",
    }