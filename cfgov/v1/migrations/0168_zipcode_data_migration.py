# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-23 14:03
from __future__ import unicode_literals

from django.db import migrations


def migrate_zipcodes(apps, schema_editor):
    """Transfer integer-based ZIP codes as strings with leading zeros."""

    EventPage = apps.get_model('v1', 'EventPage')
    for page in EventPage.objects.all():
        _zip = page.venue_zip
        if _zip:
            if len(str(_zip)) < 5:
                page.venue_zipcode = str(_zip).zfill(5)
            else:
                page.venue_zipcode = str(_zip)
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0167_eventpage_venue_zipcode'),
    ]

    operations = [
        migrations.RunPython(migrate_zipcodes),
    ]
