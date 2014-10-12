# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projectenv_project_env'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectenv',
            old_name='project_env',
            new_name='properties',
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='name',
            field=models.CharField(default=b'unknown', max_length=20),
        ),
    ]
