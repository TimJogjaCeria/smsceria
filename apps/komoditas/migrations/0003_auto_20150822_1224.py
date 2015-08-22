# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0002_auto_20150822_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barang',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
