# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0004_auto_20150822_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jenis',
            options={'verbose_name_plural': 'Jenis'},
        ),
    ]
