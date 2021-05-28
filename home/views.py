from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib import messages


class Home(View):
    @staticmethod
    def get(request):
        main_slider = Slider.objects.filter(main_slider=True)
        second_slider = Slider.objects.filter(second_slider=True)
        third_slider = Slider.objects.filter(third_slider=True)
        return render(request, 'home/index.html',
                      {'main_slider': main_slider, 'second_slider': second_slider, 'third_slider': third_slider})


class AboutUs(View):
    def get(self, request):
        return render(request, 'home/about-us.html')


class Compare(View):
    def get(self, request):
        return render(request, 'home/compare.html')


class Favorite(View):
    def get(self, request):
        return render(request, 'home/favorite.html')


class Contact(View):
    form_class = ContactForm
    template_name = 'home/contact.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactModel.objects.create(name=cd['name'], email=cd['email'], subject=cd['subject'],
                                        message=cd['message'])
            messages.success(request, 'با موفقیت ثبت شد', 'info')
            return redirect('home:contact')
        return render(request, self.template_name, {'form': form})
