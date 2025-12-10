from django.urls import path
from .views import (
    LessonListCreateAPIView,
    LessonRetrieveUpdateDestroyAPIView,
    # Или отдельные классы:
    # LessonListAPIView, LessonCreateAPIView, и т.д.
)

urlpatterns = [
    # Вариант 1: Объединенные эндпоинты (рекомендуется)
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(),
         name='lesson-detail'),

    # Вариант 2: Отдельные эндпоинты для каждой операции
    # path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    # path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    # path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    # path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    # path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]