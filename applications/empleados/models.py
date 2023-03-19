from django.db import models
from applications.departamento.models import Departamento

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=32)
    # TODO: Define fields here

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad



class Empleado(models.Model):

    JOB_TYPE = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINITRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    first_name = models.CharField('Nombre', max_length=32)
    last_name = models.CharField('Apellido', max_length=32)
    full_name = models.CharField(
        'Nombre Completo', 
        max_length=64,
        blank=True
    )
    job = models.CharField('Puesto', max_length=1, choices=JOB_TYPE)
    image = models.ImageField(
        'Avatar', 
        upload_to='empleado', blank=True, null=True,
        height_field=None, width_field=None, max_length=None
    )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
