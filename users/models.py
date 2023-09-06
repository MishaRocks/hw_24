from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    telephone = models.CharField(max_length=50, verbose_name='телефон')
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} ({self.first_name} {self.first_name})'

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
