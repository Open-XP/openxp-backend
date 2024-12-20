# Generated by Django 4.2.7 on 2024-05-25 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0016_alter_waec_total_questions'),
        ('quiz_manager', '0005_userscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='correct_questions',
            field=models.ManyToManyField(blank=True, related_name='correct_in_scores', to='exams.questions'),
        ),
        migrations.AddField(
            model_name='userscore',
            name='incorrect_questions',
            field=models.ManyToManyField(blank=True, related_name='incorrect_in_scores', to='exams.questions'),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='test_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_scores', to='quiz_manager.testinstance'),
        ),
    ]
