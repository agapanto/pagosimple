# Generated by Django 2.1 on 2018-10-29 01:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_framework_apicontrol', '__first__'),
        ('accounts', '0003_auto_20181010_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('created', 'created'), ('cancelled_by_user', 'cancelled_by_user'), ('cancelled_by_timeout', 'cancelled_by_timeout'), ('cancelled_by_gateway', 'cancelled_by_gateway'), ('completed', 'completed')], max_length=32)),
                ('payment_type', models.CharField(choices=[('single_payment', 'single_payment'), ('plan_subscription', 'plan_subscription'), ('plan_renewal', 'plan_renewal'), ('products_order', 'products_order')], max_length=32)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_framework_apicontrol.App')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]