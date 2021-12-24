from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class connection_model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    text = models.TextField()

    def __str__(self):
        return self.name


choise = (("BTC", "BTC"), ("ETH", "ETH"), ("BNB", "BNB"), ("ADA", "ADA"), ("SOL", "SOL"), ("XRP", "XRP"))


class crypto_model(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True)
    field = MultiSelectField(choices=choise, max_length=23)

class mobile_number_model(models.Model):
    rel = models.OneToOneField(crypto_model , on_delete=models.CASCADE , primary_key=True)
    mobile = PhoneNumberField(max_length=11 , null=False, blank=False, unique=True)

class price_model(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    BTC = models.CharField(max_length=40 , null=True , blank=True)
    ETH = models.CharField(max_length=40 , null=True , blank=True)
    BNB = models.CharField(max_length=40 , null=True , blank=True)
    ADA = models.CharField(max_length=40 , null=True , blank=True)
    SOL = models.CharField(max_length=40 , null=True , blank=True)
    XRP = models.CharField(max_length=40 , null=True , blank=True)

