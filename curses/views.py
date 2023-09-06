from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from curses.models import Curs
from curses.serializers import CursSerializer


class CursViewSet(ModelViewSet):
    queryset = Curs.objects.all()
    serializer_class = CursSerializer
