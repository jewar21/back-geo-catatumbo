from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from .constants import TYPES_PRODUCERS_CHOICES, MUNICIPALITY_CHOICES

# Create your models here.


class TypeProducer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=TYPES_PRODUCERS_CHOICES)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=MUNICIPALITY_CHOICES)

    def __str__(self):
        return self.name


class UserProducer(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dependency = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    type_producer = models.ForeignKey(
        TypeProducer, on_delete=models.CASCADE, related_name='user_producers')
    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, related_name='user_producers')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
