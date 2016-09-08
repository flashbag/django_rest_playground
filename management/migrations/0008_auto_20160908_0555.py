# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20160908_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.UserStatus'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.UserType'),
        ),
    ]