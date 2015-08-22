# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stok', models.DecimalField(default=0, null=True, max_digits=15, decimal_places=2)),
                ('price', models.DecimalField(default=0, null=True, max_digits=15, decimal_places=2)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Barang',
            },
        ),
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Komoditas',
            },
        ),
        migrations.CreateModel(
            name='Komoditas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Komoditas',
            },
        ),
        migrations.AddField(
            model_name='jenis',
            name='komoditas',
            field=models.ForeignKey(related_name='komoditas_jenis', to='komoditas.Komoditas'),
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis',
            field=models.ForeignKey(related_name='harganya', to='komoditas.Jenis'),
        ),
        migrations.AddField(
            model_name='barang',
            name='user',
            field=models.ForeignKey(related_name='hargaku', to='profil.Profile'),
        ),
    ]
