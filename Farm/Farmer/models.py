from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    COMMODITY_CHOICES = [
        ('Wheat', 'Wheat'),
        ('Rice', 'Rice'),
        ('Pulses', 'Pulses'),
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Farmers are users
    commodity = models.CharField(max_length=100, choices=COMMODITY_CHOICES)  # Added choices here
    quantity = models.FloatField()
    farmerprice = models.DecimalField(max_digits=10, decimal_places=2)
    baseprice = models.DecimalField(max_digits=10, decimal_places=2)
    soldquantity = models.FloatField(default=0)

    def available_quantity(self):
        return self.quantity - self.soldquantity

    def __str__(self):
        return f"{self.commodity} - {self.farmer.username}"


