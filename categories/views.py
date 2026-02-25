# categories/views.py
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# List all categories / Create new category
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view, only auth can create

# Retrieve, update, delete a single category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]  # Only auth users can update/delete