from django.urls import path
from .views import product_list, product_create, product_update, product_delete
from .views import farmer_dashboard, handle_bid, farmer_bid_list, farmer_register, FarmerLoginView


urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
    path('farmer/bids/', farmer_bid_list, name='farmer_bid_list'),
    path('farmer/handle-bid/<int:bid_id>/<str:action>/', handle_bid, name='handle_bid'),    path("dashboard/", farmer_dashboard, name="farmer_dashboard"),
    path('register/', farmer_register, name='farmer_register'),
    path('login/', FarmerLoginView.as_view(), name='farmer_login'),

]
