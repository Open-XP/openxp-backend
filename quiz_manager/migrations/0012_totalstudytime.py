# Generated by Django 4.2.7 on 2024-05-27 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_manager', '0011_alter_testinstance_subject_alter_testinstance_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalStudyTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Overall_study_time', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_study_time', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]