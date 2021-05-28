from django.db import models
from django.utils.safestring import mark_safe


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام ')
    email = models.EmailField(verbose_name='ایمیل ')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Slider(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام ')
    image = models.ImageField(upload_to='slider/%Y/%m/%d/', verbose_name='تصویر')
    description = models.CharField(max_length=100, verbose_name='توضیحات ')
    discount = models.CharField(max_length=50, verbose_name='تخفیف')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
