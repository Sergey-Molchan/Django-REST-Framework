from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                 'phone', 'city', 'avatar', 'date_joined']
        read_only_fields = ['date_joined']



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Кастомный сериализатор для JWT токена"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем в токен дополнительные поля
        token['email'] = user.email
        token['tg_name'] = user.tg_name  # если есть такое поле
        token['is_staff'] = user.is_staff

        return token