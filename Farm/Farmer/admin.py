from django.contrib import admin
from .models import Product, FarmerProfile

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'quantity', 'farmerprice', 'baseprice')
    search_fields = ('commodity',)
    list_filter = ('commodity',)

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'farmer_license_number')
    search_fields = ('user__username', 'farmer_license_number')
