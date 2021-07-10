# Generated by Django 3.2.3 on 2021-07-09 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0003_rename_clientes_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Bancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField()),
                ('estado', models.CharField(choices=[('1', 'Activa'), ('2', 'Inactiva')], default='1', max_length=1)),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=8)),
                ('propietario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_financiera.cliente')),
            ],
        ),
    ]