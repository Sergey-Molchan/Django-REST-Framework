from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from .models import Payment
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer



class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payment"""

    # Добавляем дополнительные поля для удобства
    user_email = serializers.ReadOnlyField(source='user.email')
    course_title = serializers.ReadOnlyField(source='course.title', default=None)
    lesson_title = serializers.ReadOnlyField(source='lesson.title', default=None)

    class Meta:
        model = Payment
        fields = [
            'id',
            'user',
            'user_email',  # чтобы видеть email пользователя
            'payment_date',
            'course',
            'course_title',  # чтобы видеть название курса
            'lesson',
            'lesson_title',  # чтобы видеть название урока
            'amount',
            'payment_method',
        ]
        read_only_fields = ['user', 'payment_date']  # эти поля только для чтения

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class PaymentListAPIView(generics.ListAPIView):
    """Список платежей с фильтрацией и сортировкой"""
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
    ordering = ['-payment_date']


class MyTokenObtainPairView(TokenObtainPairView):
    """Эндпоинт для получения JWT токена"""
    serializer_class = MyTokenObtainPairSerializer
