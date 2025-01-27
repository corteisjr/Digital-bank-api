from decimal import Decimal 
from datetime import datetime


from user.utils.viewsets import AbstractViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user.models import User
from rest_framework.decorators import action
from wallet.models import Wallet, Transfer
from .serializers import WalletSerializer, TransferSerializer


class WalletViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def retrieve(self, request, pk=None):
        wallet = Wallet.objects.get(user=request.user)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)


    @action(detail=False, methods=['post'])
    def add_balance(self, request):
        amount = request.data.get('amount')
        if not amount or float(amount) <= 0:
            return Response({
                'error': "Valor inválido"}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        wallet, created = Wallet.objects.get_or_create(user=request.user) 
        wallet.balance += Decimal(str(amount))
        wallet.save()
        
        return Response(
            {"message": "Saldo adicionado com sucesso",  "new_balance": wallet.balance}
                
        )
        

class TransferViewset(AbstractViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        transfers = Transfer.objects.filter(from_user=request.user)

        # Filtro por período de data (opcional)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            transfers = transfers.filter(date__range=(start_date, end_date))

        serializer = TransferSerializer(transfers, many=True)
        return Response(serializer.data)

    def create(self, request):
        to_user_id = request.data.get('to_user')
        amount = request.data.get('amount')
        
        if not to_user_id or not amount:
            return Response(
                {
                    "error": "Dados incompletos"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        try:
            to_user = User.objects.get(id=to_user_id)
        except User.DoesNotExist:
            return Response({
                'error': "Usuário destinatário não encontrado"
            }, status=status.HTTP_404_NOT_FOUND)
            
        from_user_wallet = Wallet.objects.get(user=request.user)
        to_user_wallet = Wallet.objects.get(user=to_user)
        
        if from_user_wallet.balance < Decimal(amount):
            return Response({"error": "Saldo insuficiente"}, status=status.HTTP_400_BAD_REQUEST)
        
        transfer = Transfer.objects.create(
            from_user = request.user,
            to_user = to_user, 
            amount = amount
        )
        
        from_user_wallet.balance -= Decimal(amount)
        to_user.balance += Decimal(amount)
        from_user_wallet.save()
        to_user_wallet.save()
        
        serializer = TransferSerializer(transfer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
