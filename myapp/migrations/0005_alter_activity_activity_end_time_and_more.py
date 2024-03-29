# Generated by Django 5.0.2 on 2024-03-24 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_activity_sign_up_print_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 3, 47723, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 10, 217455, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='score_open_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 12, 609133, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='sign_up_end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 14, 510096, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='sign_up_print_end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 17, 363649, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='sign_up_start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 14, 7, 19, 909067, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
