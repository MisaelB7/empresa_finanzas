from django.contrib import admin
from .models import Cliente, Cuenta_Bancaria, Depositar

# Register your models here.
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'saldo', 'propietario',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido',)

admin.site.register(Depositar)

admin.site.register(Cliente,ClienteAdmin)

admin.site.register(Cuenta_Bancaria,CuentaAdmin)
