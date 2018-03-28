# Generated by Django 2.0.3 on 2018-03-28 02:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_framework_apicontrol', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('customer_id', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_framework_apicontrol.App')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('email', 'app'), ('customer_id', 'app')},
        ),
    ]
