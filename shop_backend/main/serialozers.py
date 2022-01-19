from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, TokenSerializer, UserSerializer
from .models import Category, Product, ProductShots, Review, Rating, Profile


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод всех категорий товара"""

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


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("user", "text", "children")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = ('text', 'product', 'parent')

    def create(self, validated_data):
        review = Review.objects.create(
            user=self.context['request'].user,
            text=validated_data.get('text', None),
            parent=validated_data.get('parent', None),
            product=validated_data.get('product', None),
        )
        return review


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ("star", "product")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            user=self.context['request'].user,
            product=validated_data.get('product', None),
            defaults={
                'star': validated_data.get('star', None),
            }
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
