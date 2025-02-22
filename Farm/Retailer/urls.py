from django.urls import path
from .views import retailer_dashboard, retailer_bids, start_bid, retailer_register , RetailerLoginView

urlpatterns = [
    path('dashboard/', retailer_dashboard, name='retailer_dashboard'),  # ✅ Show products
    path('bids/', retailer_bids, name='retailer_bids'),  # ✅ Show placed bids
    path('bid/<int:product_id>/', start_bid, name='start_bid'),  
    path('register/', retailer_register, name='retailer_register'),
    path('login/', RetailerLoginView.as_view(), name='retailer_login'),

]
