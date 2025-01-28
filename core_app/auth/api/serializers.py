from rest_framework import serializers
from core_app.user.api.serializers import UserSerializer
from core_app.user.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128,
                                     min_length=8, write_only=True, 
                                     required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        if api_settings.UPDATE_LAST_LOGIN:  
            update_last_login(None, self.user)
            
        return data