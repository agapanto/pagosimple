# Generated by Django 2.1 on 2018-10-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_auto_20181008_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='renewal_options',
            field=models.ManyToManyField(blank=True, to='plans.RenewalOption'),
        ),
    ]