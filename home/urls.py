from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about-us', views.AboutUs.as_view(), name='about-us'),
    path('compare', views.Compare.as_view(), name='compare'),
    path('favorite', views.Favorite.as_view(), name='favorite'),
    path('contact', views.Contact.as_view(), name='contact'),
]
