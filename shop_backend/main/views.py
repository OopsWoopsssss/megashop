from django.db import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .serialozers import CategoryListSerializer, ProductListSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .models import Category, Product, Rating
from .service import get_client_ip


class CategoryListView(generics.ListAPIView):
    """Вывод всех категорий"""
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class ProductListView(APIView):
    """Вывод всех продуктов"""

    def get(self, request):
        product = Product.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        serializer = ProductListSerializer(product, many=True)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Добавление отзыва к продукту"""

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStarRatingViewSet(ModelViewSet):
    """Добавление рейтинга продукту"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

