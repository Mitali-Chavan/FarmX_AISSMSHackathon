from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['commodity', 'quantity', 'farmerprice', 'baseprice', 'product_photo']
        widgets = {
            'baseprice': forms.NumberInput(attrs={'readonly': 'readonly'})  # Make it read-only in the template
        }
    commodity = forms.ChoiceField(choices=Product.COMMODITY_CHOICES)  # Accessing choices from the model

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FarmerProfile

class FarmerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    farmer_license_number = forms.CharField(max_length=50, required=True)
    farmer_photo = forms.ImageField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','farmer_photo')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user, 
                phone_number=self.cleaned_data['phone_number'],
                farmer_license_number=self.cleaned_data['farmer_license_number'],
                farmer_photo=self.cleaned_data['farmer_photo']
            )
        return user
