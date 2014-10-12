# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20141012_0440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectenv',
            old_name='name',
            new_name='project_name',
        ),
        migrations.AddField(
            model_name='projectenv',
            name='team_name',
            field=models.CharField(default=b'unknown', max_length=20),
            preserve_default=True,
        ),
    ]
