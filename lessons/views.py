from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Lesson
from .serializers import LessonSerializer


# 1. Получение списка уроков И создание нового урока
class LessonListCreateAPIView(generics.ListCreateAPIView):
    """
    Generic класс для:
    - GET: получения списка всех уроков
    - POST: создания нового урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Автоматически назначаем владельца при создании"""
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            # Для тестирования без авторизации
            serializer.save()


# 2. Получение одного урока, обновление, удаление
class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic класс для:
    - GET: получения конкретного урока по ID
    - PUT: полного обновления урока
    - PATCH: частичного обновления урока
    - DELETE: удаления урока
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]




class LessonListAPIView(generics.ListAPIView):
    """Только список уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonCreateAPIView(generics.CreateAPIView):
    """Только создание урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Только получение одного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Только обновление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Только удаление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]
