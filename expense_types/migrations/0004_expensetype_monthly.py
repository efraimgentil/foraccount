# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0003_auto_20160112_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetype',
            name='monthly',
            field=models.BooleanField(default=False),
        ),
    ]
