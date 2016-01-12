# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0002_expensetype_user'),
        ('expenses', '0002_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(default=1, to='expense_types.ExpenseType'),
            preserve_default=False,
        ),
    ]
