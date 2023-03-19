# Generated by Django 4.1.5 on 2023-01-22 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=32, verbose_name='Apellido')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINITRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Puesto')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]