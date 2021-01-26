from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from mptt.models import MPTTModel


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True,
                                     verbose_name='دسته بندی')
    is_sub = models.BooleanField(default=False, verbose_name='زیردسته بندی')
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name='نام')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug, ])


class Product(models.Model):
    STATUS = (
        ('موجود', 'موجود'),
        ('ناموجود', 'ناموجود')
    )
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=200, verbose_name='نام', blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='تصویر')
    description = RichTextUploadingField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    status = models.CharField(choices=STATUS, max_length=120, verbose_name='وضعیت کالا')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده')
    updated = models.DateTimeField(auto_now=True, verbose_name='بروزرسانی شده')
    new = models.BooleanField(default=False, verbose_name='افزودن به محصولات جدید')
    are_selling = models.BooleanField(default=False, verbose_name='درحال فروش')
    future = models.BooleanField(default=False, verbose_name='محصولات آینده')

    class Meta:
        ordering = ('name',)
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug, ])

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    title = models.CharField(max_length=50, blank=True, verbose_name='عنوان')
    image = models.ImageField(blank=True, upload_to="image", verbose_name='تصویر')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصاویر'
        verbose_name_plural = 'تصاویر'
