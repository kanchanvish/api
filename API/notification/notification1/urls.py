from django.urls import path,include
from .views import *
urlpatterns = [
    path('notification',NotificationView.as_view())
]