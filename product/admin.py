from django.contrib import admin
from product.models import *

admin.site.site_header = " پنل اصلی "


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 4


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
