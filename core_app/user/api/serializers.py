from core_app.user.models import User
from core_app.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'created',
            'updated'
        ]

        read_only = ['is_active']
