# Generated by Django 3.2.7 on 2021-09-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=8000),
        ),
    ]
