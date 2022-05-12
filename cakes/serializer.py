from rest_framework import serializers
from .models import Cakes


class CakesSerializer(serializers.ModelSerializer):
    """Serializer for the cake model"""
    class Meta:
        model = Cakes
        fields = '__all__'