from django.db import models
from django.contrib.auth.models import User
from Farmer.models import Product

class Bid(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    retailer = models.ForeignKey(User, on_delete=models.CASCADE)  # The retailer who placed the bid
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # The product being bid on
    bid_price = models.FloatField()  # The price offered by the retailer
    bid_quantity = models.FloatField()  # The quantity retailer wants
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # Status of the bid

    def __str__(self):
        return f"{self.retailer.username} - {self.product.commodity} - {self.status}"


from django.db import models
from django.contrib.auth.models import User

class RetailerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    retailer_license_number = models.CharField(max_length=50)
    retailer_photo = models.ImageField(upload_to='retailer_images/', null=True, blank=True)


    def __str__(self):
        return self.user.username
