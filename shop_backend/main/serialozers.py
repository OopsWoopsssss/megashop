from rest_framework import serializers
from .models import Category, Product, ProductShots


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод всех категорий товара"""

    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """Вывод всех товаров"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'poster', 'price', 'category',)


class ProductShotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = ("image", )


class ProductDetailSerializer(serializers.ModelSerializer):
    """Вывод конкретного товаров"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    shots = ProductShotsListSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
