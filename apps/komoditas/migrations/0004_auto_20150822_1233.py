# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0003_auto_20150822_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='barang',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
