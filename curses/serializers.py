from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from curses.models import Curs
from lessons.models import Lesson


class CursSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_count(self, curs):
        return Lesson.objects.filter(curs=curs.pk).count()

    def get_lessons(self, curs):
        return [curs.title for curs in Lesson.objects.filter(curs=curs)]

    class Meta:
        model = Curs
        fields = ('title', 'lessons_count', 'lessons')
