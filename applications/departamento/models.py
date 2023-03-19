from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=32)
    short_name = models.CharField('Nombre Corto', max_length=32)
    status = models.BooleanField('Estatus', default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Departamento."""

        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of Departamento."""
        return str(self.id) + '-' + self.name + '-' + self.short_name