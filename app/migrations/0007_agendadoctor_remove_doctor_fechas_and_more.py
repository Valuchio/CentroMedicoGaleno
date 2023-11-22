# Generated by Django 4.0.1 on 2023-11-21 21:22

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_fechaconsulta_remove_doctor_fechas_doctor_fechas'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Insira uma data para agenda', validators=[app.models.validar_dia])),
                ('horario', models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='fechas',
        ),
        migrations.DeleteModel(
            name='FechaConsulta',
        ),
        migrations.AddField(
            model_name='agendadoctor',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor'),
        ),
        migrations.AddField(
            model_name='agendadoctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterUniqueTogether(
            name='agendadoctor',
            unique_together={('horario', 'dia')},
        ),
    ]
