from django.urls import path
from .views import CategoryListView, ProductListView, ReviewCreateView, AddStarRatingViewSet, CartListView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('cart/', CartListView.as_view()),
    path("review/", ReviewCreateView.as_view({'post': 'create'})),
    path("rating/", AddStarRatingViewSet.as_view({'post': 'create'})),
]
