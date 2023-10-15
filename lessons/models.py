from django.db import models

# Create your models here.
from users.models import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='curs/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_link = models.CharField(max_length=100, verbose_name='Ссылка на видео', **NULLABLE)
    curs = models.ForeignKey(to='curses.Curs', on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок',
        verbose_name_plural = 'Уроки'
