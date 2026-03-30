from django.db import models
from config import settings


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='courses/preview',blank=True, null=True, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание',blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses',verbose_name='Владелец')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
