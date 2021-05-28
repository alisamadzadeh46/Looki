from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from .models import *


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['name']


