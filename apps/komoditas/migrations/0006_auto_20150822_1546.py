# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('komoditas', '0005_auto_20150822_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='user',
            field=models.ForeignKey(related_name='hargaku', to=settings.AUTH_USER_MODEL),
        ),
    ]
