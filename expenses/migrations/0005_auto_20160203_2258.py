# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0006_auto_20160203_2241'),
        ('expenses', '0004_expense_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='subtype',
            field=models.ForeignKey(related_name='expense_subtypes', default=1, to='expense_types.ExpenseType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(related_name='expense_types', to='expense_types.ExpenseType'),
        ),
    ]
