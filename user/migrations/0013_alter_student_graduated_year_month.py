# Generated by Django 5.0.2 on 2024-03-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_sex_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduated_year_month',
            field=models.DateField(),
        ),
    ]
