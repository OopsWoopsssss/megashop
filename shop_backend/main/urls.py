from django.urls import path
from .views import ProductSet

urlpatterns = [
    path('product/', ProductSet.as_view()),
]