from rest_framework import routers
from wallet.api.viewsets import WalletViewSet

router = routers.SimpleRouter()

router.register(r'wallet', WalletViewSet, basename='wallet')


urlpatterns = [
    *router.urls,
]
