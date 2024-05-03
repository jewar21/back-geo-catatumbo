from rest_framework import serializers
from GeoAPIs.models import UserProductorDb
        
class UserProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProductorDb
        fields="__all__" # Incluye todos los campos del modelo