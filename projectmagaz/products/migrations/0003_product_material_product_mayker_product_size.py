# Generated by Django 4.1.2 on 2023-02-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_prace_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(default='Бавовна', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='mayker',
            field=models.CharField(default='Китай', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='M', max_length=5),
        ),
    ]
