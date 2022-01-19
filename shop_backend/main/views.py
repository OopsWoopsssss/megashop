from django.db import models
from djoser.views import UserViewSet
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .serialozers import (
    CategoryListSerializer,
    ProductListSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
)
from .models import Category, Product, Profile
from .service import get_client_ip


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

