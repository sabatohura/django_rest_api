from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT, SET_NULL
class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32,blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name="transactions")
    date = models.DateTimeField
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True, related_name="transactions")
    def __str__(self):
        return f"{self.amount} {self.currency.code} {self.date}"

class User(models.Model):
    username = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=12,blank=True)
    fullname = models.TextField(blank=False)
    def __str__(self):
        return f"{self.username} {self.location} {self.phone} {self.fullname}"

class imageProfile(models.Model):
    imagename = models.CharField(max_length=100, blank=False)
    userId = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name="users")
    uploadedate = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.imagename} {self.userId} {self.uploadedate}"

