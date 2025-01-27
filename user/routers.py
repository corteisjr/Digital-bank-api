from rest_framework import routers
from user.api.viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *router.urls,
]
