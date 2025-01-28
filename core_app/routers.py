from rest_framework import routers
from core_app.auth.api.viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet
from core_app.user.api.viewsets import UserViewSet
from core_app.wallet.api.viewsets import WalletViewSet, TransferViewset

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'wallet', WalletViewSet, basename='wallet')
router.register(r'transfer', TransferViewset, basename='transfer')




urlpatterns = [
    *router.urls,
]
