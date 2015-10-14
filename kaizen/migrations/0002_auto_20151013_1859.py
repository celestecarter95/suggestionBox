# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(default=b'new', max_length=3, choices=[(b'new', b'New'), (b'den', b'Denied'), (b'rev', b'In Review'), (b'2do', b'To Do'), (b'imp', b'Implemented')]),
        ),
    ]
