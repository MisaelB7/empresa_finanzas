from app_financiera.models import Cliente, Cuenta_Bancaria, Depositar
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from decimal import Decimal


# Create your views here.

@login_required()
def index(request):
     return render(request, 'financiera/index.html')

@login_required()
def deposito(request):
     
     if request.method == 'POST':
        dep = Cuenta_Bancaria.objects.get(pk=request.user.cliente.cuenta_bancaria.pk)
        monto = Decimal(request.POST.get('monto'))
        deposito = Depositar(monto=monto, cuenta=dep)
        deposito.save()
        cuenta = Cuenta_Bancaria.objects.filter(pk=request.user.cliente.cuenta_bancaria.pk).first()
        cuenta.saldo= cuenta.saldo + monto
        cuenta.save()      
        return redirect('/')

     return render(request, 'financiera/deposito.html')
  
@login_required()
def retiro(request):
     
     if request.method == 'POST':
        dep = Cuenta_Bancaria.objects.get(pk=request.user.cliente.cuenta_bancaria.pk)
        monto = Decimal(request.POST.get('monto'))
        deposito = Depositar(monto=monto, cuenta=dep)
        deposito.save()
        cuenta = Cuenta_Bancaria.objects.filter(pk=request.user.cliente.cuenta_bancaria.pk).first()
        cuenta.saldo= cuenta.saldo - monto
        cuenta.save()      
        return redirect('/')

     return render(request, 'financiera/retiro.html')
