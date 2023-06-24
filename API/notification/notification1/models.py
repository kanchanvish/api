from django.db import models

# Create your models here.
class NotificationModel(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=1000)
    read = models.BooleanField(default=False, editable=True)
