from django.db import models
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .serialozers import (
    CategoryListSerializer,
    ProductListSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    CartListSerializer,
)
from .models import Category, Product, Cart


class CategoryListView(generics.ListAPIView):
    """Вывод всех категорий"""
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class ProductListView(APIView):
    """Вывод всех продуктов"""

    def get(self, request):
        product = Product.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__user=request.user.id))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        serializer = ProductListSerializer(product, many=True)
        return Response(serializer.data)


class ReviewCreateView(ModelViewSet):
    """Добавление отзыва к продукту"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class AddStarRatingViewSet(ModelViewSet):
    """Добавление рейтинга продукту"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save()


class CartListView(generics.GenericAPIView):
    """Корзина"""

    def get(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(owner__id=user.id)
        serializer = CartListSerializer(cart)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(owner__id=user.id)


