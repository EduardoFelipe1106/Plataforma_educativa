# Generated by Django 4.0 on 2022-09-20 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Simulador_examenes', '0006_alter_pregunta_tipo_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='user',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='area_pregunta',
            field=models.CharField(choices=[('RAZONAMIENTO MATEMÁTICO', 'Razonamiento Matemático'), ('RAZONAMIENTO VERBAL', 'Razonamiento Verbal')], default='RAZONAMIENTO MATEMATICO', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='categoria_pregunta',
            field=models.CharField(choices=[('PNP', 'Policia Nacional del Perú')], default='PNP', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='frecuencia_pregunta',
            field=models.IntegerField(choices=[(100, '100%')], default=100),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='nivel_pregunta',
            field=models.CharField(choices=[('GENERAL', 'Nivel de pregunta General')], default='GENERAL', max_length=30),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='programa_pregunta',
            field=models.CharField(choices=[('ESCPOGRA', 'ESCPOGRA'), ('ESCUELA DE FORMACIÓN', 'ESCUELA DE FORMACIÓN')], default='ESCPOGRA', max_length=100),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.CharField(choices=[('Virtual Practica', 'Virtual - Practica'), ('Virtual Practica', 'Practica')], default='Virtual Practica', max_length=50),
        ),
    ]
