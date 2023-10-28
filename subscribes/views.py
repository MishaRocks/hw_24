from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curses.models import Curs
from curses.serializers import CursSerializer
from subscribes.models import Subscribe
from subscribes.serializers import SubscribeSerializer

from tasks import send_subscription_notification, send_unsubscription_notification, send_course_update_notification


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Curs.objects.all()

    def create(self, request, *args, **kwargs):
        curs = self.get_object()  # Получаем объект курса из URL
        user = request.user

        # Проверяем не подписан ли пользователь уже на этот курс
        if Subscribe.objects.filter(user=user, curs=curs).exists():
            return Response({"detail": "Вы уже подписаны на этот курс."}, status=status.HTTP_400_BAD_REQUEST)
        # Создаем подписку
        subscription = Subscribe(user=user, curs=curs)
        subscription.save()

        send_subscription_notification.delay(user.email, curs.title)

        return Response({"detail": "Подписка успешно установлена."}, status=status.HTTP_201_CREATED)


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Subscribe.objects.filter(user=user, is_active=True)

    def perform_destroy(self, request, curs_id):
        user = request.user
        # Устанавливаем подписку как неактивную вместо фактического удаления
        subscribe = Subscribe.objects.filter(curs=curs_id, user=user).first()
        subscribe.is_active = False
        subscribe.save()

        send_unsubscription_notification.delay(subscribe.user.email, subscribe.curs.title)

        return Response({"detail": "Вы отписаны."}, status=status.HTTP_201_CREATED)
