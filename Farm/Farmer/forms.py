from django import forms
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['commodity', 'quantity', 'farmerprice', 'product_photo']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FarmerProfile

class FarmerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    farmer_license_number = forms.CharField(max_length=50, required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user, 
                phone_number=self.cleaned_data['phone_number'],
                farmer_license_number=self.cleaned_data['farmer_license_number'],
            )
        return user
