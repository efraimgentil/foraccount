# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0003_profit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit',
            name='father_profit',
            field=models.ForeignKey(related_name='related_profits', default=1, blank=True, to='profits.Profit'),
            preserve_default=False,
        ),
    ]
