# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0004_expensetype_monthly'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetype',
            name='global_expense_type',
            field=models.ForeignKey(related_name='subtypes', to='expense_types.ExpenseType', null=True),
        ),
    ]
