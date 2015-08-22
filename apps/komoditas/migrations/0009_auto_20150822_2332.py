# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0008_auto_20150822_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='latitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='longitude',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
