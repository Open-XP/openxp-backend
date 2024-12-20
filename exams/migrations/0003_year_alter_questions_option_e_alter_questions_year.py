# Generated by Django 4.2.7 on 2024-05-23 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_questions_image_alter_questions_option_e'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_E',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='year',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.PROTECT, related_name='years', to='exams.year'),
        ),
    ]
