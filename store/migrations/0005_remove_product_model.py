# Generated by Django 3.2.8 on 2021-10-11 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
    ]
