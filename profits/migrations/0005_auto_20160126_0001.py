# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0004_profit_father_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit',
            name='father_profit',
            field=models.ForeignKey(related_name='related_profits', blank=True, to='profits.Profit', null=True),
        ),
    ]
