from django import forms
from django.shortcuts import render, get_object_or_404, redirect

from Retailer.models import Bid
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Retailer.models import Bid
from .models import Product  # Farmer's products

@login_required
def farmer_dashboard(request):
    farmer_products = Product.objects.filter(farmer=request.user)  
    bids = Bid.objects.filter(product__in=farmer_products).select_related("retailer", "product")

    return render(request, "Farmer/farmer_dashboard.html", {
        "farmer_products": farmer_products,
        "bids": bids,
    })

from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from Retailer.models import Bid

def handle_bid(request, bid_id, action):
    bid = get_object_or_404(Bid, id=bid_id)

    if action == "accept":
        bid.status = "Accepted"
        bid.save()
        messages.success(request, f"Bid for {bid.product.commodity} has been accepted!")
    elif action == "reject":
        messages.info(request, f"Bid for {bid.product.commodity} has been rejected.")
        bid.delete()  # Delete the rejected bid

    return redirect('farmer_bid_list')  # Redirect farmer to bids page



from django.shortcuts import render, get_object_or_404
from .models import Product

def farmer_bid_list(request):
    farmer_products = Product.objects.filter(farmer=request.user)
    bids = Bid.objects.filter(product__in=farmer_products)  # Removed `.order_by('-timestamp')`

    return render(request, 'Farmer/farmer_bids.html', {'bids': bids})

