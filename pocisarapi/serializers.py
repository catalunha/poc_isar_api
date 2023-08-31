from rest_framework import serializers

from .models import Data1Model


class Data1Serializer(serializers.Serializer):
    class Meta:
        model = Data1Model
        fields = ['id', 'name', 'age']
