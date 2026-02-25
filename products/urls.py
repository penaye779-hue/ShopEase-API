# products/urls.py
from django.urls import path
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    # List all products / Create new product
    path('', ProductListCreateView.as_view(), name='product-list-create'),

    # Retrieve, update, delete a single product by ID
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]