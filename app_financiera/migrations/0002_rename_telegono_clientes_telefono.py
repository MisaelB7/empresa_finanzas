# Generated by Django 3.2.3 on 2021-07-09 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_financiera', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='telegono',
            new_name='telefono',
        ),
    ]
