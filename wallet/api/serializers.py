from rest_framework import serializers
from user.utils.serializers import AbstractSerializer
from wallet.models import Wallet, Transfer
from user.api.serializers import UserSerializer


class WalletSerializer(AbstractSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']


class TransferSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Transfer
        fields = ['id', 'from_user', 'to_user', 'amount', 'date']