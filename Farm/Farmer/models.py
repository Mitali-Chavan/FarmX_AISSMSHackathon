from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    COMMODITY_CHOICES = [
        ('Wheat', 'Wheat'),
        ('Rice', 'Rice'),
        ('Pulses', 'Pulses'),
    ]

    BASE_PRICE_DEFAULTS = {
        'Wheat': 25.00,
        'Rice': 30.00,
        'Pulses': 50.00,
    }

    farmer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    commodity = models.CharField(max_length=100, choices=COMMODITY_CHOICES)
    quantity = models.FloatField()
    farmerprice = models.DecimalField(max_digits=10, decimal_places=2)
    baseprice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    soldquantity = models.FloatField(default=0)
    product_photo = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.baseprice:
            self.baseprice = self.BASE_PRICE_DEFAULTS.get(self.commodity, 25.00)
        super().save(*args, **kwargs)

    def available_quantity(self):
        return self.quantity - self.soldquantity

    def __str__(self):
        return f"{self.commodity} - {self.farmer.username}"

from django.db import models
from django.contrib.auth.models import User

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    farmer_license_number = models.CharField(max_length=50)

    
    def __str__(self):
        return self.user.username
