# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141011_0451'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DockerDB',
            new_name='ProjectEnv',
        ),
    ]
