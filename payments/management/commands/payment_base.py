import json

from django.core.management import BaseCommand
from django.db import connection

from payments.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open('payment_data.json', 'r', encoding='UTF8') as file:
            payment_data = json.load(file)

        for p in payment_data:
            if 'curs' in p:
                Payment.objects.create(
                    curs_id=p['curs'],
                    pay_sum=p['pay_sum'],
                    pay_method=p['pay_method']
                )
            else:
                Payment.objects.create(
                    lesson_id=p['lesson'],
                    pay_sum=p['pay_sum'],
                    pay_method=p['pay_method']
                )
