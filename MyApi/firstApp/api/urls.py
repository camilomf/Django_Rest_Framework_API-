from .views import firstFunction
from .views import CarSpecsViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car-specs',CarSpecsViewSet, basename='car-specs')

urlpatterns = [
    path('first/',firstFunction),
    path('',include(router.urls)),
]