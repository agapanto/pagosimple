from django.db import migrations


def create_default_renewal_options(apps, schema_editor):
    # We can't import the Currency model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    RenewalOption = apps.get_model('plans', 'RenewalOption')

    default_renewal_options_data = [
        {
            'code': '1MONTH',
            'name': '1 month',
            'discount': 0,
            'renewal_period_count': 1,
            'renewal_period_type': 'months',
        },
        {
            'code': '3MONTHS',
            'name': '3 months',
            'discount': 0,
            'renewal_period_count': 3,
            'renewal_period_type': 'months',
        },
        {
            'code': '6MONTHS',
            'name': '6 months',
            'discount': 0,
            'renewal_period_count': 6,
            'renewal_period_type': 'months',
        },
        {
            'code': '1YEAR',
            'name': '1 year',
            'discount': 0,
            'renewal_period_count': 1,
            'renewal_period_type': 'years',
        },
    ]

    for renewal_option_data in default_renewal_options_data:
        renewal_option = RenewalOption.objects.create(**renewal_option_data)


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0008_planinstance_account'),
    ]

    operations = [
        migrations.RunPython(create_default_renewal_options),
    ]
