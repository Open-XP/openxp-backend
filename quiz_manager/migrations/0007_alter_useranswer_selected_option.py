# Generated by Django 4.2.7 on 2024-05-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_manager', '0006_userscore_correct_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='selected_option',
            field=models.CharField(blank=True, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D'), ('E', 'Option E')], max_length=1, null=True),
        ),
    ]
