# Generated by Django 5.0.2 on 2024-03-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_activitystudents_is_checked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitystudents',
            name='checked_number',
            field=models.IntegerField(blank=True, default=113001),
            preserve_default=False,
        ),
    ]
