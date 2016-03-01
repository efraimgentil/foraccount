# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_auto_20160203_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='subtype',
            field=models.ForeignKey(related_name='expense_subtypes', to='expense_types.ExpenseType', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(related_name='expense', to='expense_types.ExpenseType'),
        ),
    ]
