from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
         self.fecha_publicacion = timezone.now()
         self.save()
    
    def __str__(self):
         return self.titulo

class paises(models.Model):
    
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    cantidades_hab = models.TextField()
    cuidades_imp = models.TextField()
    lugares_tur = models.TextField()
    imagen = models.ImageField(upload_to='paises/', null=True, blank=True)
    idi = models.CharField(max_length=200, default='Español')
    moneda = models.CharField(max_length=200, default='Español')
    superficie =models.CharField(max_length=200, default='Español')
    imagenes_lug1 = models.ImageField(upload_to='paises/', null=True, blank=True)
    imagenes_lug2 = models.ImageField(upload_to='paises/', null=True, blank=True)
    imagenes_lug3 = models.ImageField(upload_to='paises/', null=True, blank=True)
    
    
def __str__(self):
    return self.titulo