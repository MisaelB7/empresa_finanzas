# Generated by Django 3.2.3 on 2021-07-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0004_cuenta_bancaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta_bancaria',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
