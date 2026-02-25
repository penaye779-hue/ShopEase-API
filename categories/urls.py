# categories/urls.py
from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    # List all categories / Create new category
    path('', CategoryListCreateView.as_view(), name='category-list-create'),

    # Retrieve, update, delete a single category by ID
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]