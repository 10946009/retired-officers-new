# Generated by Django 5.0.2 on 2024-04-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_scorelabel_score1_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='score2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='score3',
            field=models.FloatField(default=0),
        ),
    ]