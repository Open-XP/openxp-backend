# Generated by Django 4.2.7 on 2024-05-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_alter_questions_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(default=2010),
        ),
    ]
