# Generated by Django 5.1.6 on 2025-02-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Retailer', '0003_retailerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailerprofile',
            name='retailer_photo',
            field=models.ImageField(blank=True, null=True, upload_to='retailer_images/'),
        ),
    ]
