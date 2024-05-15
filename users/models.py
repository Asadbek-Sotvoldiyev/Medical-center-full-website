from django.db import models
from django.contrib.auth.models import User
from medical.models import BaseModel


class Letter(BaseModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user} {self.created_time.date}"

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
