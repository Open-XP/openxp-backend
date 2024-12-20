# Generated by Django 3.1 on 2024-06-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0021_auto_20240610_1141'),
        ('quiz_manager', '0016_auto_20240610_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinstance',
            name='questions',
            field=models.ManyToManyField(to='exams.Questions'),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='correct_questions',
            field=models.ManyToManyField(blank=True, related_name='correct_in_scores', to='exams.Questions'),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='incorrect_questions',
            field=models.ManyToManyField(blank=True, related_name='incorrect_in_scores', to='exams.Questions'),
        ),
    ]
