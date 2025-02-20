from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['commodity', 'quantity', 'farmerprice', 'baseprice']

    commodity = forms.ChoiceField(choices=Product.COMMODITY_CHOICES)  # Accessing choices from the model
