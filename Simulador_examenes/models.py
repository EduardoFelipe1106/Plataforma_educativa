from asyncio.windows_events import NULL
from concurrent.futures.process import _threads_wakeups
from pyexpat import model
from re import T
from django.db import models
from .choices import programa, categoria, area, tema, respuesta, niveles, frecuencia, tipo
from django.contrib.auth.models import User

# Create your models here.

class pregunta(models.Model):
    categoria_pregunta = models.CharField(max_length = 100, choices=categoria, default='PNP')
    programa_pregunta = models.CharField(max_length=100, choices=programa, default='ESCPOGRA')
    area_pregunta = models.CharField(max_length=100, choices=area, default='RAZONAMIENTO MATEMATICO')
    tema_pregunta = models.CharField(max_length=100, choices=tema, default='N/A')
    texto_pregunta = models.TextField(blank=True)
    alternativa_primera = models.CharField(max_length=100, blank=True)
    alternativa_segunda = models.CharField(max_length=100, blank=True)
    alternativa_tercera = models.CharField(max_length=100, blank=True)
    alternativa_cuarta = models.CharField(max_length=100, blank=True)
    alternativa_quinta = models.CharField(max_length=100, blank=True)
    respuesta_pregunta = models.CharField(max_length=1, choices=respuesta, blank=False)
    nivel_pregunta = models.CharField(max_length=30, choices=niveles, default='GENERAL')
    frecuencia_pregunta = models.IntegerField(choices=frecuencia, default=100)
    tipo_pregunta = models.CharField(max_length=50, choices=tipo, default='Virtual Practica')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=NULL)

    def __str__(self):
        return 'Pregunta de ' + self.tema_pregunta