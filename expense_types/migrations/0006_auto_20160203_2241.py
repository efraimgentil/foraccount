# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0005_expensetype_global_expense_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensetype',
            old_name='global_expense_type',
            new_name='father_expense_type',
        ),
    ]
