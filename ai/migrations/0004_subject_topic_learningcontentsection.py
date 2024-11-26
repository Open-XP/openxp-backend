# Generated by Django 4.2.15 on 2024-09-01 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ai', '0003_alter_chatsession_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='ai.subject')),
            ],
        ),
        migrations.CreateModel(
            name='LearningContentSection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=20)),
                ('difficulty', models.CharField(max_length=2)),
                ('section_type', models.CharField(choices=[('introduction', 'Introduction'), ('learning_objectives', 'Learning Objectives'), ('core_concepts', 'Core Concepts'), ('step_by_step', 'Step-by-Step Explanations'), ('examples', 'Examples'), ('practice_problems', 'Practice Problems'), ('interactive_elements', 'Interactive Elements'), ('summary', 'Summary'), ('reflection_questions', 'Reflection Questions'), ('additional_resources', 'Additional Resources')], max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_content_sections', to='ai.subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_content_sections', to='ai.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_content_sections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'subject', 'topic', 'grade', 'section_type')},
            },
        ),
    ]
