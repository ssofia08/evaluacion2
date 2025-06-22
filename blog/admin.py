from django.contrib import admin
from .models import paises
from .models import Publicacion

admin.site.register(Publicacion)
admin.site.register(paises)