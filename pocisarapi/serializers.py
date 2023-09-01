from rest_framework import serializers

from .models import Data1Model


class Data1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Data1Model
        fields = ['id', 'name', 'age']
