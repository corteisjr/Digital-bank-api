from rest_framework import routers
from auth.api.viewsets import (
     RegisterViewSet, 
     LoginViewSet, 
     RefreshViewSet
)
    

router = routers.SimpleRouter()

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


urlpatterns = [
    *router.urls,
]
