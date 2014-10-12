# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141011_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectenv',
            name='pydocker',
        ),
        migrations.AddField(
            model_name='projectenv',
            name='name',
            field=models.CharField(default=b'unknwon_name', max_length=20),
            preserve_default=True,
        ),
    ]
