from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class connection_model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    text = models.TextField()

    def __str__(self):
        return self.name


choise = (("BTC", "BTC"), ("ETH", "ETH"), ("BNB", "BNB"), ("ADA", "ADA"), ("SOL", "SOL"), ("XRP", "XRP"))


class crypto_model(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    field = MultiSelectField(choices=choise, max_length=23)


