from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    # image = models.ImageField(upload_to='home')
    def __str__(self):
        return self.username