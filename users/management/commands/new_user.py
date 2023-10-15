from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='tehobox@yand.ru',
            first_name='Misha',
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        user.set_password('qwerty')
        user.save()
