from rest_framework import serializers

from curses.models import Curs


class CursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curs
        fields = '__all__'
