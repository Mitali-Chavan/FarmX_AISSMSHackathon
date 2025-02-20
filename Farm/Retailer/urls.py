from django.urls import path
from .views import retailer_dashboard, retailer_bids, start_bid

urlpatterns = [
    path('dashboard/', retailer_dashboard, name='retailer_dashboard'),  # ✅ Show products
    path('bids/', retailer_bids, name='retailer_bids'),  # ✅ Show placed bids
    path('bid/<int:product_id>/', start_bid, name='start_bid'),  
]
