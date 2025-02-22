from django import forms
from .models import Bid

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price', 'bid_quantity']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RetailerProfile

class RetailerSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    retailer_license_number = forms.CharField(max_length=50, required=True)
    retailer_photo = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','retailer_photo')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            RetailerProfile.objects.create(
                user=user, 
                phone_number=self.cleaned_data['phone_number'],
                retailer_license_number=self.cleaned_data['retailer_license_number'],
                retailer_photo = self.cleaned_data['retailer_photo']

            )
        return user
