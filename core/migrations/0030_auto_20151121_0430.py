# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20151121_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationrestaurant',
            name='company_id',
            field=models.ForeignKey(to='core.Company'),
        ),
    ]
