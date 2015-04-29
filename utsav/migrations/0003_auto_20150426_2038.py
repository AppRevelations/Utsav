# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utsav', '0002_auto_20150425_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fest_id',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
