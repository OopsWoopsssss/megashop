from rest_framework import serializers
from .models import Category, Product, ProductShots


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод всех категорий товара"""
    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """Вывод всех товаров"""
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
    """Вывод конкретного товаров"""
    class Meta:
        model = Product
        fields = "__all__"