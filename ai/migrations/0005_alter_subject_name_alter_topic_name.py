# Generated by Django 4.2.15 on 2024-09-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0004_subject_topic_learningcontentsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
