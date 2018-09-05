from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Wallet(models.Model):
    currency = models.CharField(max_length=3)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
