# Generated by Django 4.2.7 on 2024-05-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_manager', '0008_userscore_total_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='total_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]