from rest_framework import viewsets

from .serializers import Data1Serializer
from .models import Data1Model


class Data1ViewSet(viewsets.ModelViewSet):
    queryset = Data1Model.objects.all()
    serializer_class = Data1Serializer
