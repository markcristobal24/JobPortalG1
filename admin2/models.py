from django.db import models
from users.models import User

# Create your models here.
class Admin2(models.Model):
    pass

class ActivityLog(models.Model):
    user = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.activity_type} by {self.user}"