# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0007_auto_20150822_1607'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='barang',
            unique_together=set([('user', 'jenis')]),
        ),
    ]
