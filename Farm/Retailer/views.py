from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  
from .models import Bid
from Farmer.models import Product

# ✅ View 1: Retailer Dashboard (Shows available products)
def retailer_dashboard(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'retailer_dashboard.html', {'products': products})

# ✅ View 2: Retailer Bids Page (Shows their placed bids)
@login_required
def retailer_bids(request):
    retailer_bids = Bid.objects.filter(retailer=request.user).select_related("product")
    return render(request, "retailer_bids.html", {"retailer_bids": retailer_bids})

# ✅ View 3: Start Bidding
@login_required
def start_bid(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        bid_amount = request.POST.get("bid_amount")
        bid_quantity = request.POST.get("bid_quantity")

        if not bid_amount or not bid_quantity:
            return render(request, "start_bid.html", {
                "product": product,
                "error": "Bid amount and quantity are required."
            })

        Bid.objects.create(
            product=product,
            retailer=request.user,  # ✅ Fix: Use logged-in retailer
            bid_price=bid_amount,
            bid_quantity=bid_quantity
        )

        return redirect('retailer_bids')  # ✅ Redirect to bids page after placing a bid

    return render(request, "start_bid.html", {"product": product})


from django.shortcuts import render, redirect
from .forms import RetailerSignUpForm

def retailer_register(request):
    if request.method == 'POST':
        form = RetailerSignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This now saves both User and RetailerProfile
            return redirect('retailer_login')  # Adjust as needed
    else:
        form = RetailerSignUpForm()
    return render(request, 'retailer/register.html', {'form': form})


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product

class RetailerLoginView(LoginView):
    template_name = "retailer/login.html"

    def get_success_url(self):
        return reverse_lazy('retailer_dashboard')  # Redirect to retailer_dashboard

