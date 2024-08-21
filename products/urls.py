# products/urls.py

from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy, product_list, product_create, product_update, product_delete

urlpatterns = [
    # Rute API
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

    # Rute untuk tampilan front-end
    path('', product_list, name='product-list'),
    path('products/add/', product_create, name='product-create'),
    path('products/<int:pk>/edit/', product_update, name='product-edit'),
    path('products/<int:pk>/delete/', product_delete, name='product-delete'),
]
