from django.shortcuts import render
from django.http import JsonResponse
from Farmer.models import Product
from Retailer.models import Bid

def home(request):
    return render(request, 'home/home.html')

def update_ribbon(request):
    products = Product.objects.all()
    
    data = []
    for product in products:
        highest_accepted_bid = Bid.objects.filter(product=product, status='Accepted').order_by('-bid_price').first()
        highest_farmers_accepted_price = highest_accepted_bid.bid_price if highest_accepted_bid else "N/A"

        data.append({
            "commodity": product.commodity,
            "base_price": float(product.baseprice),
            "highest_farmers_accepted_price": float(highest_farmers_accepted_price) if highest_farmers_accepted_price != "N/A" else "N/A",
        })
    
    return JsonResponse(data, safe=False)


from django.shortcuts import render

def auth_choice(request):
    return render(request, 'home/choose_auth.html')


from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirects to home after logout



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Farmer.models import FarmerProfile
from Retailer.models import RetailerProfile

@login_required
def profile(request):
    user = request.user
    farmer_profile = None
    retailer_profile = None

    # Try to get the farmer profile if it exists
    try:
        farmer_profile = FarmerProfile.objects.get(user=user)
    except FarmerProfile.DoesNotExist:
        pass

    # Try to get the retailer profile if it exists
    try:
        retailer_profile = RetailerProfile.objects.get(user=user)
    except RetailerProfile.DoesNotExist:
        pass

    context = {
        'user': user,
        'farmer_profile': farmer_profile,
        'retailer_profile': retailer_profile,
    }
    return render(request, 'profile.html', context)


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')