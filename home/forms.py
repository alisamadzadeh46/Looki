from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), error_messages={
        'required': "لطفا نام خود را وارد کنید"
    })
    email = forms.EmailField(widget=forms.EmailInput(), error_messages={'required': "لطفا ایمیل خود را وارد کنید"})
    subject = forms.CharField(widget=forms.TextInput(), error_messages={'required': "لطفا ایمیل خود را وارد کنید"})
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'pb-10'}),
                              error_messages={'required': "لطفا متن پیام خود را وارد کنید"})
