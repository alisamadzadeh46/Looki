from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.Products.as_view(), name='show_product'),
]
