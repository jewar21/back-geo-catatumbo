from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User


from .constants import TYPES_PRODUCERS_CHOICES, MUNICIPALITY_CHOICES

# Create your models here.

class UserProductorDb(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dependency = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type_producer = models.CharField(
        max_length=50, choices=TYPES_PRODUCERS_CHOICES)
    municipality = models.CharField(
        max_length=50, choices=MUNICIPALITY_CHOICES)


# class RegistroArborizacion(models.Model):
#     tipo_intervencion = models.CharField(max_length=100)
#     familia = models.CharField(max_length=100)
#     latitud = models.FloatField()
#     longitud = models.FloatField()
#     nombre_cientifico = models.CharField(max_length=100)
#     genero = models.CharField(max_length=10)
#     estado_conservacion = models.CharField(max_length=20)
#     coordenada_y = models.FloatField()
#     coordenada_x = models.FloatField()
#     altura = models.FloatField()
#     origen = models.CharField(max_length=100)
#     fecha_intervencion = models.DateField()
#     nombre_comun = models.CharField(max_length=100)
#     estado = models.CharField(max_length=20)