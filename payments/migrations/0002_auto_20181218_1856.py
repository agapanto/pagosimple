# Generated by Django 2.1.4 on 2018-12-18 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='status',
            new_name='payment_status',
        ),
    ]