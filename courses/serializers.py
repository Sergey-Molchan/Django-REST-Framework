from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_lessons_count(self, obj):
        """Возвращает количество уроков в курсе"""
        return obj.lessons.count()
