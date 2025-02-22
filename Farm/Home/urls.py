from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, update_ribbon, auth_choice, logout_view, profile

urlpatterns = [
    path('', home, name='home'),
    path('update-ribbon/', update_ribbon, name='update_ribbon'),
    path('auth/', auth_choice, name='auth_choice'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),

]

# Serve static and media files **only in development**
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
