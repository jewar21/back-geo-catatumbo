from django.contrib import admin
from .models import TypeProducer, Municipality, UserProducer

# Register your models here.
admin.site.register(TypeProducer)
admin.site.register(Municipality)
admin.site.register(UserProducer)
