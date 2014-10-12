# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141011_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectenv',
            name='project_env',
            field=jsonfield.fields.JSONField(default=__builtin__.dict),
            preserve_default=True,
        ),
    ]
