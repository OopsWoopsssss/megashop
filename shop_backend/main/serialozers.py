from abc import ABC

from rest_framework import serializers
from .models import Category, Product, ProductShots, Review, Rating


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод всех категорий товара"""

    products_categories = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)

    class Meta:
        model = Category
        fields = "__all__"


class ProductShotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = ("image",)


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ("star", "product")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            product=validated_data.get('product', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


class ProductListSerializer(serializers.ModelSerializer):
    """Вывод всех товаров"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    shots = ProductShotsListSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"
