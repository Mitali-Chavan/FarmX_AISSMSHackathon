from django.urls import path
from .views import home, update_ribbon

urlpatterns = [
    path('', home, name='home'),
    path('update-ribbon/', update_ribbon, name='update_ribbon'),
]
