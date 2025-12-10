from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Простейший сериализатор для урока"""

    class Meta:
        model = Lesson
        fields = '__all__'  # Все поля модели
        read_only_fields = ['owner', 'created_at', 'updated_at']