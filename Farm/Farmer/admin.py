from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'quantity', 'farmerprice', 'baseprice')
    search_fields = ('commodity',)
    list_filter = ('commodity',)
