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
            product = form.save(commit=False)
            product.farmer = request.user  # Assign the current user
            product.save()
            return redirect('product_list')
        else:
            print(form.errors)  # Debug: Print any form errors in the console
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
    product = bid.product  # Get the associated product

    if action == "accept":
        print(f"Before Acceptance: Available = {product.available_quantity()}, Sold = {product.soldquantity}, Bid Quantity = {bid.bid_quantity}")

        # Check if there's enough quantity left to fulfill the bid
        if product.available_quantity() >= bid.bid_quantity:
            bid.status = "Accepted"
            bid.save()

            # Deduct the sold quantity from the product
            product.soldquantity += bid.bid_quantity
            product.save()

            print(f"After Acceptance: Available = {product.available_quantity()}, Sold = {product.soldquantity}")


            messages.success(request, f"Bid for {bid.product.commodity} has been accepted!")
        else:
            messages.error(request, f"Not enough stock available for {bid.product.commodity}.")
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

from django.shortcuts import render, redirect
from .forms import FarmerSignUpForm

def farmer_register(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)  # Removed request.FILES
        if form.is_valid():
            form.save()
            return redirect('farmer_login')
    else:
        form = FarmerSignUpForm()
    return render(request, 'farmer/register.html', {'form': form})

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class FarmerLoginView(LoginView):
    template_name = "farmer/login.html"
    
    def get_success_url(self):
        # Assumes you have a URL pattern named 'product_list'
        return reverse_lazy('product_list')
