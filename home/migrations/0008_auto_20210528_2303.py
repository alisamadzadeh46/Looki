# Generated by Django 3.1.5 on 2021-05-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210528_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='main_slider',
            field=models.BooleanField(default=False, verbose_name='اسلایدر اصلی'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='second_slider',
            field=models.BooleanField(default=False, verbose_name='دومین اسلایدر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='third_slider',
            field=models.BooleanField(default=False, verbose_name='سومین اسلایدر'),
        ),
    ]
