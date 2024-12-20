# Generated by Django 4.2.7 on 2024-05-23 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0002_questions_image_alter_questions_option_e'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.waec')),
                ('questions', models.ManyToManyField(to='exams.questions')),
                ('subjects', models.ManyToManyField(to='exams.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_option', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D'), ('E', 'Option E')], max_length=1)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.questions')),
                ('test_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz_manager.testinstance')),
            ],
        ),
    ]
