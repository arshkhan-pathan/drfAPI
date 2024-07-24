import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, )
    is_Pending = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name