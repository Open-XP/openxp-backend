# Generated by Django 4.2.13 on 2024-07-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examscheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examscheduler',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
