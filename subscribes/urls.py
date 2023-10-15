from django.urls import path

from subscribes.apps import SubscribesConfig
from subscribes.views import SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = SubscribesConfig.name

urlpatterns = [
    path('<int:pk>/create/', SubscribeCreateAPIView.as_view(), name='Subscribe-create'),
    path('<int:pk>/delete/', SubscribeDestroyAPIView.as_view(), name='Subscribe-delete'),
]
