from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .form import *
from .models import Profile


class Register(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            Profile.objects.create(user=user)
            messages.success(request, 'حساب کاربری با موفقیت ساخت شد.لطفا وارد شوید', 'info')
            return redirect('account:register')
        return render(request, self.template_name, {'form': form})
