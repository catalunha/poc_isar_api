from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import Data1ViewSet

routes = SimpleRouter()
routes.register('data1', Data1ViewSet, basename='data1')

urlpatterns = [
    path('', include(routes.urls))
]
