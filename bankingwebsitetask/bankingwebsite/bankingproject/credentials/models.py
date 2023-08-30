from django.db import models
import datetime


class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    dob = models.DateField(default=datetime.date.today)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.username


class Account(models.Model):
    account_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_number


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
