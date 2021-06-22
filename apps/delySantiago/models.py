from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.IntegerField()
    
    def __str__(self):
        return self.nombre
        
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    ingredientes = models.TextField()
    descripcion = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="platos", null=True)
    
    def __str__(self):
        return self.nombre
