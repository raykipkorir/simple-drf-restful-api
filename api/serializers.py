from rest_framework import serializers

from app.models import Drink

class DrinkSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        data =  Drink.objects.create(**validated_data)
        return data
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.save()
        return instance
