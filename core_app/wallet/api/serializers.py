from core_app.abstract.serializers import AbstractSerializer
from core_app.wallet.models import Wallet, Transfer
from core_app.user.api.serializers import UserSerializer


class WalletSerializer(AbstractSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']


class TransferSerializer(AbstractSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Transfer
        fields = ['id', 'from_user', 'to_user', 'amount', 'date']