# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_types', '0002_expensetype_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetype',
            name='description',
            field=models.TextField(max_length=200, blank=True),
        ),
    ]
