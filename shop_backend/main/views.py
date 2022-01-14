from django.db import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serialozers import CategoryListSerializer, ProductListSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .models import Category, Product
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
            middle_star=models.Sum(models.F('ratings__star__value')) / models.Count(models.F('ratings'))
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


class AddStarRatingView(APIView):
    """Добавление рейтинга продукту"""

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
