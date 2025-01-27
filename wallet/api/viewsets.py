from user.utils.viewsets import AbstractViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from wallet.models import Wallet, Transfer
from .serializers import WalletSerializer, TransferSerializer


class WalletViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = WalletSerializer

    def retrieve(self, request, pk=None):
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)


    @action(detail=False, methods=['post'])
    def add_balance(self, request):
        amount = request.data.get('amount')
        if not amount or float(amount) <= 0:
            return Response({'error': "Valor inválido"}, status=status.HTTP_400_BAD_REQUEST)
        
        wallet = Wallet.objects.get(user=request.user)
        wallet.balance += float(amount)
        wallet.save()
        
        return Response(
            {"message": "Saldo adicionado com sucesso",  "new_balance": wallet.balance}
                
        )
        
