from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Course, Lesson
from .serializers import CourseSerializer
from lessons.serializers import LessonSerializer


# 1. ViewSet для курсов (как в задании)
class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для курсов"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# 2. Generic-классы для уроков (как в задании!)
class LessonListCreateAPIView(generics.ListCreateAPIView):
    """Generic класс: список уроков + создание"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Generic класс: получение + обновление + удаление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]