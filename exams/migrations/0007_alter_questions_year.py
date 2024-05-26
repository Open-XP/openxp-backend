# Generated by Django 4.2.7 on 2024-05-23 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20240523_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='years', to='exams.year'),
        ),
    ]