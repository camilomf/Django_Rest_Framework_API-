from rest_framework import serializers
from firstApp.models import CarSpecs

class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['car_brand','car_model','production_year','car_body','engine_type']