from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length = 30)
    tipo = models.CharField(max_length = 30)
    porciones = models.FloatField(default = 0)
    ing_y_cant = models.CharField(max_length = 30)
    procedimiento = models.CharField(max_length = 30)
    is_active = models.BooleanField(default = True)
    image_recetas = models.ImageField(upload_to = 'image_recetas', blank = True , null = True)

    class Meta:
        verbose_name = 'receta'
        verbose_name_plural = 'recetas'

    def __str__(self):
        return self.nombre