# Generated by Django 2.1 on 2018-10-10 02:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
