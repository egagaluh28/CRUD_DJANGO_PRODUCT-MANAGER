# product_manager/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  # Rute untuk API
    path('', include('products.urls')),  # Rute untuk tampilan frontend
]