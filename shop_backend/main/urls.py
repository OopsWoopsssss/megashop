from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]