from django.urls import path

from lessons.apps import LessonsConfig
from lessons.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = LessonsConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('', LessonListAPIView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]
