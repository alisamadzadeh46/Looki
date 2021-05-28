from .models import Profile
from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages={'required': "لطفا نام کابری خود را وارد کنید"},
                               widget=forms.TextInput(attrs={'class': 'form-control-plaintext dir-ltr'}))
    email = forms.EmailField(error_messages={'required': "لطفا ایمیل خود را  وارد کنید"},
                             widget=forms.EmailInput(attrs={'class': 'form-control-plaintext dir-ltr'}))
    password = forms.CharField(error_messages={'required': "لطفا رمزعبور خود را  وارد کنید"},
                               widget=forms.PasswordInput(attrs={'class': 'form-control-plaintext dir-ltr'}))
