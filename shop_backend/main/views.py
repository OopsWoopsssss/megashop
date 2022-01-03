from .models import Category, Product, ProductShots
from rest_framework import generics
from .serialozers import CategoryListSerializer, ProductListSerializer, ProductDetailSerializer


class CategoryListView(generics.ListAPIView):
    """Вывод всех категорий"""
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class ProductListView(generics.ListAPIView):
    """Вывод всех продуктов"""
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    """Вывод продукта"""
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
