# Generated by Django 4.2.7 on 2023-12-31 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_question_subject_alter_question_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exams.topic'),
        ),
    ]
