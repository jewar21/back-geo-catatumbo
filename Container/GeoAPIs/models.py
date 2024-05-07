from django.db import models
from db_connection import get_mongo_client, get_database

from .constants import TYPES_PRODUCERS_CHOICES, MUNICIPALITY_CHOICES

client = get_mongo_client()
database = get_database(client)

# Create your models here.

class UserProductorDb(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False)
    lastname = models.CharField(max_length=100, verbose_name="Apellido", blank=False, null=False)
    dependency = models.CharField(max_length=100, verbose_name="Dependencia", blank=False, null=False)
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico", blank=False, null=False)
    password = models.CharField(max_length=128, verbose_name="Contraseña", blank=False, null=False)
    type_producer = models.CharField(
        max_length=50, choices=TYPES_PRODUCERS_CHOICES, verbose_name="Tipo de productor", blank=False, null=False)
    municipality = models.CharField(
        max_length=50, choices=MUNICIPALITY_CHOICES, verbose_name="Municipio", blank=False, null=False)

    class Meta:
        db_table = 'Producers'
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    @classmethod
    def save_object(cls, instance, *args, **kwargs):
        database.insert_one(instance.__dict__)

    def __str__(self) -> str:
        return self.name


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