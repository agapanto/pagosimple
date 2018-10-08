from django.db import migrations


def create_default_currencies(apps, schema_editor):
    # We can't import the Currency model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Currency = apps.get_model('currencies', 'Currency')

    default_currencies_data = [
        {
            'name': 'Dollar',
            'symbol': '$',
            'code': 'USD',
            'conversion_factor': 1,
            'enabled': True,
        },
        {
            'name': 'Chilean peso',
            'symbol': '$',
            'code': 'CLP',
            'conversion_factor': 1,
            'enabled': False,
        },
    ]

    for currency_data in default_currencies_data:
        currency = Currency.objects.create(**currency_data)


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_currencies),
    ]
