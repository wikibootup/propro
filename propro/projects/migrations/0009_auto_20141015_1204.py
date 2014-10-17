# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20141012_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectenv',
            name='project_name',
            field=models.CharField(default=b'none', unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='team_name',
            field=models.CharField(default=b'none', unique=True, max_length=20),
        ),
    ]
