from django.shortcuts import render



def home(request):
    return render(request, 'home/home.html')  # Use 'home/home.html' to keep templates organized


from django.http import JsonResponse
from Farmer.models import Product

def update_ribbon(request):
    products = Product.objects.all()
    data = [
        {
            "commodity": product.commodity,
            "latest_price": product.farmerprice,  # Adjust based on your model
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)
