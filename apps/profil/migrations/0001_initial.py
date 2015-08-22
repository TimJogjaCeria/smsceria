# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True, choices=[(b'L', b'Laki-laki'), (b'P', b'Perempuan')])),
                ('phone_number', models.CharField(max_length=100, null=True, blank=True)),
                ('latitude', models.CharField(max_length=100, null=True)),
                ('longitude', models.CharField(max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
