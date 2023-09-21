from rest_framework import serializers

from lessons.models import Lesson
from lessons.validators import ValidatorLinks


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [ValidatorLinks(field='description')]
