# Generated by Django 5.1.6 on 2025-02-22 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0007_alter_product_baseprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerprofile',
            name='farmer_photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_photo',
        ),
    ]
