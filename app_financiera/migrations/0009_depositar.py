# Generated by Django 3.2.3 on 2021-07-10 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0008_cliente_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depositar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=4, max_digits=12)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_financiera.cuenta_bancaria')),
            ],
        ),
    ]
