from django.contrib import admin
from .models import Cliente, Cuenta_Bancaria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cuenta_Bancaria)