from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'home/index.html')


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
    def get(self, request):
        return render(request, 'home/contact.html')
