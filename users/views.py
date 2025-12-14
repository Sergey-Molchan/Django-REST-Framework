from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для пользователей (дополнительное задание).
    Позволяет выполнять CRUD операции с пользователями.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]