# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-04 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('some_name', '0002_payment_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.NullBooleanField(),
        ),
    ]