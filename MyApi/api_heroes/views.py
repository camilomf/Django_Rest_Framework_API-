from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Heroe
from .serializers import HeroesSerializer
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

@permission_classes([AllowAny])
class HeroeAPIView(APIView):

    def get(self,request):
        heroe = Heroe.objects.all()
        serializer = HeroesSerializer(heroe,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = HeroesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class HeroeDetailAPIView(APIView):
    
    def get_object(self,id):
        try:
            return Heroe.objects.get(id=id)
        
        except Heroe.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        heroe = self.get_object(id)
        serializer = HeroesSerializer(heroe)
        return Response(serializer.data)

    def put(self, request, id):
        heroe = self.get_object(id)
        serializer = HeroesSerializer(heroe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        heroe = self.get_object(id)
        heroe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)