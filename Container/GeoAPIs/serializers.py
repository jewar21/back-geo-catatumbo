from rest_framework import serializers
from GeoAPIs.models import UserProductorDb
        
class UserProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProductorDb
        fields=['email', 'password', 'name', 'lastname']
        extra_fields = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return UserProductorDb.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user