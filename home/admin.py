from django.contrib import admin

from .models import *

admin.site.index_title = "پنل مدیریتی"


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']
    readonly_fields = ('image_tag',)
