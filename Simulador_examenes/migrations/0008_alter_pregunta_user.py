# Generated by Django 4.0 on 2022-09-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Simulador_examenes', '0007_pregunta_user_alter_pregunta_area_pregunta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
