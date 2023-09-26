from django.db import models


class Subscribe(models.Model):

    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    curs = models.ForeignKey(to='curses.Curs', on_delete=models.CASCADE, verbose_name='Курс')
    is_active = models.BooleanField(default=True, verbose_name='Подписка')

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
