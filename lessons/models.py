# lessons/models.py - ИСПРАВЛЕННАЯ ВЕРСИЯ
from django.db import models
from django.conf import settings
# УДАЛИ ЭТУ СТРОКУ: from courses.models import Course (она больше не нужна)

class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(
        max_length=200,
        verbose_name='Название урока'
    )

    description = models.TextField(
        verbose_name='Описание урока'
    )

    preview = models.ImageField(
        upload_to='lessons/previews/',
        blank=True,
        null=True,
        verbose_name='Превью'
    )

    video_url = models.URLField(
        verbose_name='Ссылка на видео'
    )


    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс'
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='lessons',
        verbose_name='Владелец урока'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['created_at']