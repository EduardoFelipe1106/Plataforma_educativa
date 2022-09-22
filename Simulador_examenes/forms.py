from dataclasses import field
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import pregunta


class Registrar_pregunta(ModelForm):
    class Meta:
        model = pregunta
        fields = ['categoria_pregunta', 'programa_pregunta', 'area_pregunta', 'tema_pregunta', 'texto_pregunta', 
        'alternativa_primera', 'alternativa_segunda', 'alternativa_tercera', 'alternativa_cuarta', 'alternativa_quinta',
        'respuesta_pregunta', 'nivel_pregunta', 'frecuencia_pregunta', 'tipo_pregunta'
        ]

