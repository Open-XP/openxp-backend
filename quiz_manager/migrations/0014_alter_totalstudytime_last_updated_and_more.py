# Generated by Django 4.2.7 on 2024-05-28 00:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_manager', '0013_remove_totalstudytime_overall_study_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalstudytime',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='totalstudytime',
            name='overall_study_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='totalstudytime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
