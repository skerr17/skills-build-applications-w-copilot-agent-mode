
from django.db import models

class ActivityLog(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.activity_type} ({self.duration_minutes} min)"
