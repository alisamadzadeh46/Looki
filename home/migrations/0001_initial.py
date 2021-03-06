# Generated by Django 3.1.5 on 2021-01-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام ')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل ')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
    ]
