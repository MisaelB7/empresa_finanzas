from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Cuenta_Bancaria(models.Model):
    ESTADOS= (
        ('1', 'Activa'),
        ('2', 'Inactiva'),
    )
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    saldo = models.DecimalField(max_digits=12, decimal_places=4)
    propietario = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.saldo}'

class Depositar(models.Model):

    monto = models.DecimalField(max_digits=12, decimal_places=4)
    fecha = models.DateTimeField(auto_now=True)
    cuenta = models.ForeignKey(Cuenta_Bancaria, on_delete=models.CASCADE)