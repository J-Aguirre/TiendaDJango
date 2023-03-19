from django.db import models

class Prueba(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cantidad = models.IntegerField(null=True)

    def __str__(self):
        return self.titulo + '-' + self.subtitulo