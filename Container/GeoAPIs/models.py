from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from .constants import TYPES_PRODUCERS_CHOICES, MUNICIPALITY_CHOICES


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProductorDb(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        max_length=100, verbose_name="Nombre", blank=False, null=False)
    lastname = models.CharField(
        max_length=100, verbose_name="Apellido", blank=False, null=False)
    dependency = models.CharField(
        max_length=100, verbose_name="Dependencia", blank=False, null=False)
    email = models.EmailField(
        unique=True, verbose_name="Correo Electrónico", blank=False, null=False)
    password = models.CharField(
        max_length=128, verbose_name="Contraseña", blank=False, null=False)
    type_producer = models.CharField(
        max_length=50, choices=TYPES_PRODUCERS_CHOICES, verbose_name="Tipo de productor", blank=False, null=False)
    municipality = models.CharField(
        max_length=50, choices=MUNICIPALITY_CHOICES, verbose_name="Municipio", blank=False, null=False)
    is_staff = models.BooleanField(default=False) #para otorgarle acceso a las áreas administrativas.
    is_active = models.BooleanField(
        default=True, verbose_name="Estado", blank=False, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'Producers'
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'



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
