from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your models here.

class TypeProducer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProducer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    city = models.CharField(max_length=100)
    type_producer = models.ForeignKey(TypeProducer, on_delete=models.CASCADE)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)