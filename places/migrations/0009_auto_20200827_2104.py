# Generated by Django 3.1 on 2020-08-27 18:04

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('places', '0008_auto_20200827_2059'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='image',
            table='Фото',
        ),
        migrations.AlterModelTable(
            name='place',
            table='Места',
        ),
    ]
