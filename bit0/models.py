from django.db import models
from django.contrib.auth.models import User

class connection_model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    text = models.TextField()

    def __str__(self):
        return self.name

