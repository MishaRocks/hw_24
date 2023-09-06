from django.urls import path
from rest_framework.routers import DefaultRouter
from curses.apps import CursesConfig
from curses.views import CursViewSet

app_name = CursesConfig.name

router = DefaultRouter()
router.register(r'curs', CursViewSet, basename='curs')

urlpatterns = [

] + router.urls

