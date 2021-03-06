# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 05:20
from __future__ import unicode_literals

from django.db import migrations

TYPES = ["admin", "manager", "customer"]

def combine_types(apps, schema_editor):

	# We can't import the Person model directly as it may be a newer
	# version than this migration expects. We use the historical version.
	UserType = apps.get_model("management", "UserType")

	for utype in TYPES:
		user_type_model = UserType(name=utype)
		user_type_model.save()

class Migration(migrations.Migration):

	dependencies = [
		('management', '0004_user_user_status'),
	]

	operations = [
		migrations.RunPython(combine_types),
	]
