from django.db import models
from User.models import User as u


class Massage(models.Model):
    receiver = models.ForeignKey(u, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    sender = models.ForeignKey(u, on_delete=models.CASCADE, null=True, blank=True, related_name="user2")
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    see = models.BooleanField(default=False)