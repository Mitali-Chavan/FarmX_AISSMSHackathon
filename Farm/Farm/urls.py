from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),  # Home app handles the root URL
    path('farmer/', include('Farmer.urls')),
    path('retailer/', include('Retailer.urls')),
]
