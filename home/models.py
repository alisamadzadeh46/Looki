from django.db import models


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

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'
