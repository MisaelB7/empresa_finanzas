# Generated by Django 3.2.3 on 2021-07-09 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0002_rename_telegono_clientes_telefono'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
    ]
