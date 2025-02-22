# Generated by Django 5.1.6 on 2025-02-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0005_farmerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerprofile',
            name='farmer_photo',
            field=models.ImageField(blank=True, null=True, upload_to='farmer_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
