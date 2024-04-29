from rest_framework import serializers
from GeoAPIs.models import TypeProducer, UserProducer

class TypeProducerSerializers(serializers.ModelSerializer):
    class Meta:
        model=TypeProducer
        fields=['name']
        
class UserProducerSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserProducer
        fields=('name', 'email', 'password', 'city','type_producer')