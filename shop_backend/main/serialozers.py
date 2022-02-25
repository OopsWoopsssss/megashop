from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, TokenSerializer, UserSerializer
from .models import Category, Product, ProductShots, Review, Rating, Profile, Cart


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
    create_data = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = "__all__"


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

    poster_url = serializers.SerializerMethodField('get_image_url')
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    shots = ProductShotsListSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    discount_prise = serializers.SerializerMethodField('get_discount_prise')

    def get_image_url(self, obj):
        return obj.poster.url

    def get_discount_prise(self, obj):
        obj.discount_prise = obj.price - obj.price * obj.discount / 100
        return obj.discount_prise

    class Meta:
        model = Product
        fields = "__all__"


class ProductsCartSerializer(serializers.ModelSerializer):

    poster_url = serializers.SerializerMethodField('get_image_url')
    discount_prise = serializers.SerializerMethodField('get_discount_prise')

    def get_image_url(self, obj):
        return obj.poster.url

    def get_discount_prise(self, obj):
        obj.discount_prise = obj.price - obj.price * obj.discount / 100
        return obj.discount_prise

    class Meta:
        model = Product
        fields = ('title', 'poster_url','price','sale', 'discount_prise', )

class CartListSerializer(serializers.ModelSerializer):

    products = ProductsCartSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = "__all__"