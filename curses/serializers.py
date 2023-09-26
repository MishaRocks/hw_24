from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from curses.models import Curs
from lessons.models import Lesson
from subscribes.models import Subscribe


class CursSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_lessons_count(self, curs):
        return Lesson.objects.filter(curs=curs.pk).count()

    def get_lessons(self, curs):
        return [curs.title for curs in Lesson.objects.filter(curs=curs)]

    class Meta:
        model = Curs
        fields = ('title', 'lessons_count', 'lessons', 'user')

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:

            return Subscribe.objects.filter(user=request.user, course=obj, is_active=True).exists()
        return False
