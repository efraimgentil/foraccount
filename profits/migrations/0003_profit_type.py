# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0002_profittype'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit',
            name='type',
            field=models.ForeignKey(default=1, to='profits.ProfitType'),
            preserve_default=False,
        ),
    ]
