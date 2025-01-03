# Generated by Django 5.0.7 on 2024-09-24 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano de Fabricação'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Placa'),
        ),
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor'),
        ),
    ]
