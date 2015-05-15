# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movieId', models.IntegerField()),
                ('movieName', models.CharField(max_length=20)),
                ('movieType', models.CharField(max_length=20)),
                ('movieReleaseDate', models.DateTimeField()),
                ('movieLength', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
