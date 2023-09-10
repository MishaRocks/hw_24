from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet

from curses.models import Curs
from curses.serializers import CursSerializer


class CursViewSet(ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer



