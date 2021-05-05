from rest_framework import serializers
from .models import Heroe

class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroe
        fields = ['id','nombre','poder','estado']