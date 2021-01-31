from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(ContactModel, ContactAdmin)
