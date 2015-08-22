# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0006_auto_20150822_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='price',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='barang',
            name='stok',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
    ]
