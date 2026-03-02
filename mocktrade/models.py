from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    MessagePostedToday = models.IntegerField(default=0)

class Hero(models.Model):
    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=30)
    item1 = models.CharField(max_length=30)
    item2 = models.CharField(max_length=30)

class MarketRecord(models.Model):
    itemid = models.CharField(max_length=30)
