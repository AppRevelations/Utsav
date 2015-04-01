# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=256)),
                ('event_desc', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=128)),
                ('timings', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('contact_person', models.CharField(max_length=256)),
                ('contact_number', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fest_name', models.CharField(max_length=256)),
                ('fest_desc', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=128)),
                ('timings', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=256)),
                ('email_id', models.EmailField(max_length=75)),
                ('contact_number', models.CharField(max_length=20)),
                ('image_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='fest_id',
            field=models.ForeignKey(to='utsav.Fest'),
            preserve_default=True,
        ),
    ]
