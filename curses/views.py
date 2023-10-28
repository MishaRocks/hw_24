from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from curses.models import Curs
from curses.paginators import CursesPaginator
from curses.serializers import CursSerializer
from curses.permissions import ModeratorAndObjectOwner
from subscribes.models import Subscribe

from subscribes.tasks import send_course_update_notification


class CursViewSet(ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer
    pagination_class = CursesPaginator

    permission_classes = [IsAuthenticated, ModeratorAndObjectOwner]

    def perform_update(self, serializer):
        instance = serializer.save()
        # Обновляем дату последнего обновления курса
        instance.last_updated = timezone.now()
        instance.save()

        # Получаем список пользователей, подписанных на этот курс
        subscriptions = Subscribe.objects.filter(
            curs=instance,
            is_active=True
        )

        # Создаем список адресов электронной почты пользователей
        user_emails = [subscription.user.email for subscription in subscriptions]

        # Запускаем задачу отправки уведомления об обновлении курса
        send_course_update_notification.delay(instance.name, user_emails)

