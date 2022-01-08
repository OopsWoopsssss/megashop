from django.urls import path
from .views import CategoryListView, ProductListView, ReviewCreateView, AddStarRatingView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
]
