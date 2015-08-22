# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='komoditas',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
