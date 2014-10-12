# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20141012_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectenv',
            name='docker_text',
            field=models.TextField(default=b'none'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='project_name',
            field=models.CharField(default=b'none', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='team_name',
            field=models.CharField(default=b'none', max_length=20),
        ),
    ]
