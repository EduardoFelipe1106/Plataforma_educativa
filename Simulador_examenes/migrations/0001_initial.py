# Generated by Django 4.0 on 2022-09-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_pregunta', models.CharField(choices=[('PNP', 'Policia Nacional del Perú'), ('UNIVERSIDADES', 'Universidades del Perú'), ('MTC', 'Ministerio de Transporte y Comunicaciones')], default='GENERAL', max_length=100)),
                ('programa_pregunta', models.CharField(choices=[('GENERAL', 'Pregunta general'), ('PAMOID', 'Pregunta del programa PAMOID'), ('PROMACIPOL', 'Pregunta del programa PROMACIPOL'), ('DIPCOEM', 'Pregunta del programa DIPCOEM'), ('DIPOC', 'Pregunta del programa DIPOC'), ('DIPOT', 'Pregunta del programa DIPOT')], default='GENERAL', max_length=100)),
                ('area_pregunta', models.CharField(choices=[('N/A', 'Pregunta sin area'), ('RAZONAMIENTO MATEMÁTICO', 'Razonamiento Matemático'), ('RAZONAMIENTO VERBAL', 'Razonamiento Verbal')], default='N/A', max_length=100)),
                ('tema_pregunta', models.CharField(choices=[('N/A', 'Pregunta sin tema'), ('Series Numericas', 'Series Numericas'), ('Probabilidades', 'Probabilidades'), ('Porcentajes', 'Porcentajes'), ('Resolución de ecuaciones', 'Resolucion de ecuaciones'), ('Conectores Lógicos', 'Conectores Lógicos'), ('Terminos excluidos', 'Terminos excluidos'), ('Comprensión de lectura', 'Comprensión de lectura')], default='N/A', max_length=100)),
                ('texto_pregunta', models.TextField(blank=True)),
                ('alternativa_primera', models.CharField(blank=True, max_length=100)),
                ('alternativa_segunda', models.CharField(blank=True, max_length=100)),
                ('alternativa_tercera', models.CharField(blank=True, max_length=100)),
                ('alternativa_cuarta', models.CharField(blank=True, max_length=100)),
                ('alternativa_quinta', models.CharField(blank=True, max_length=100)),
                ('respuesta_pregunta', models.CharField(choices=[('A', 'Respuesta A'), ('B', 'Respuesta B'), ('C', 'Respuesta C'), ('D', 'Respuesta D'), ('E', 'Respuesta E')], max_length=1)),
                ('nivel_pregunta', models.CharField(choices=[('GENERAL', 'Nivel de pregunta General'), ('BÁSICO', 'Nivel de pregunta Básico'), ('INTERMEDIO', 'Nivel de pregunta Intermedio'), ('AVANZANDO', 'Nivel de pregunta Avanzando')], default='GENERAL', max_length=30)),
                ('frecuencia_pregunta', models.IntegerField(choices=[('10%', 10), ('25%', 25), ('50%', 50), ('75%', 75)], default=100)),
            ],
        ),
    ]
