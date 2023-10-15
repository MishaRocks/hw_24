from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from curses.models import Curs
from curses.serializers import CursSerializer
from subscribes.models import Subscribe
from subscribes.serializers import SubscribeSerializer


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

        return Response({"detail": "Подписка успешно установлена."}, status=status.HTTP_201_CREATED)


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Subscribe.objects.filter(user=user, is_active=True)

    def perform_destroy(self, instance):
        # Устанавливаем подписку как неактивную вместо фактического удаления
        instance.is_active = False
        instance.save()
