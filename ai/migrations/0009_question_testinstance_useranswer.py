# Generated by Django 4.2.15 on 2024-09-02 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ai', '0008_generatelearningcontentcontainer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ai.subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ai.topic')),
            ],
        ),
        migrations.CreateModel(
            name='TestInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('questions', models.ManyToManyField(to='ai.question')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai.subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_test_instances', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_option', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1)),
                ('is_correct', models.BooleanField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai.question')),
                ('test_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='ai.testinstance')),
            ],
        ),
    ]
