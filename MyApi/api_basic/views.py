from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import CarSpecs
from .serializers import CarSpecsSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

@permission_classes([AllowAny])
class CarSpecsAPIView(APIView):

    def get(self,request):
        car_specs = CarSpecs.objects.all()
        serializer = CarSpecsSerializer(car_specs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CarSpecsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class CarSpecsDetailAPIView(APIView):
    
    def get_object(self,id):
        try:
            return CarSpecs.objects.get(id=id)
        
        except CarSpecs.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        car_specs = self.get_object(id)
        serializer = CarSpecsSerializer(car_specs)
        return Response(serializer.data)

    def put(self, request, id):
        car_specs = self.get_object(id)
        serializer = CarSpecsSerializer(car_specs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        car_specs = self.get_object(id)
        car_specs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)