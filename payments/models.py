from django.conf import settings
from django.db import models

from users.models import NULLABLE

pay_var = [('cash', 'наличные'),
           ('cashless', 'перевод на счёт')]


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name='Даты оплаты')
    curs = models.ForeignKey(to='curses.Curs', on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    lesson = models.ForeignKey(to='lessons.Lesson', on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)
    pay_sum = models.IntegerField(verbose_name='Сумма оплаты')
    pay_method = models.CharField(max_length=30, choices=pay_var, default='перевод на счёт', verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.lesson}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
