# products/views.py
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

# Pagination class
class ProductPagination(PageNumberPagination):
    page_size = 5            # default items per page
    page_size_query_param = 'page_size'
    max_page_size = 50

# List all products & create new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Anyone can view, only auth users can create
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price', 'stock']  # filtering options
    search_fields = ['name', 'description']            # search options

# Retrieve, update, delete a single product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Anyone can view, only auth users can update/delete