from django.db import models


# Create your models here.
from users.models import NULLABLE


class Curs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(upload_to='curs/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс',
        verbose_name_plural = 'Курсы'
