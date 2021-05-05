from django.urls import path, include
from .views import HeroeAPIView, HeroeDetailAPIView

urlpatterns = [
    path('heroes/', HeroeAPIView.as_view()),
    path('heroes/<int:id>/', HeroeDetailAPIView.as_view()),
]