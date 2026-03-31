from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from lessons.serializers import LessonSerializer
from .models import Course
from lessons.models import Lesson
from .serializers import CourseSerializer



class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для курсов"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class LessonListCreateAPIView(generics.ListCreateAPIView):
    """Generic класс: список уроков + создание"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Generic класс: получение + обновление + удаление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]