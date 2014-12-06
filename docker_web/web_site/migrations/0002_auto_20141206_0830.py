# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='conid',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='port',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='islive',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
