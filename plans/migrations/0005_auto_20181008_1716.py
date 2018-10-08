# Generated by Django 2.1 on 2018-10-08 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_create_default_data'),
        ('plans', '0004_auto_20181008_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='base_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='currency',
            field=models.ForeignKey(default='USD', on_delete=django.db.models.deletion.CASCADE, to='currencies.Currency'),
        ),
    ]