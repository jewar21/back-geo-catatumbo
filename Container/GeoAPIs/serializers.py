from rest_framework import serializers
from GeoAPIs.models import TypeProducer, UserProducer

class TypeProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeProducer
        fields=['name']
        
class UserProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProducer
        fields="__all__" # Incluye todos los campos del modelo