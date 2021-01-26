# Generated by Django 3.1.5 on 2021-01-14 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210114_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی های'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'تصاویر', 'verbose_name_plural': 'تصاویر'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'محصولات', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, verbose_name='افزودن به محصولات جدید'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_sub',
            field=models.BooleanField(default=False, verbose_name='زیردسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scategory', to='product.category', verbose_name='دسته بندی'),
        ),
    ]
