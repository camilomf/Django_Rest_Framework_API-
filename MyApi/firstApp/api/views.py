apfrom rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from .serializers import CarSpecsSerializer
from firstApp.models import CarSpecs

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    print(request.query_params)
    print(request.query_params['key'])
    number = request.query_params['key']
    return Response({"message": number})

@permission_classes([AllowAny])
class CarSpecsViewSet(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs