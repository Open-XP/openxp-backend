# Generated by Django 5.0 on 2024-01-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_remove_exam_exam_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
