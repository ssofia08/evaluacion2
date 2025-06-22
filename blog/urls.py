from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_public, name=' lista_public'),
    path('evaluacion2/', views.lista_paises, name='lista_paises'),
    path('evaluacion2/pais/<int:pk>/', views.detalle_pais, name='detalle_pais'),
]
