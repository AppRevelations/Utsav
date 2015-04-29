# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utsav', '0003_auto_20150426_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
