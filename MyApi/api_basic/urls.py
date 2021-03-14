from django.urls import path, include
from .views import CarSpecsAPIView, CarSpecsDetailAPIView

urlpatterns = [
    path('car-specs/', CarSpecsAPIView.as_view()),
    path('car-specs/<int:id>/', CarSpecsDetailAPIView.as_view()),
]