from rest_framework.routers import SimpleRouter

from .views import Data1ViewSet

routes = SimpleRouter()
routes.register('data1', Data1ViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pocisarapi.urls'))
]
