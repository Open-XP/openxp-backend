# Generated by Django 4.2.15 on 2024-09-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0006_alter_learningcontentsection_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningcontentsection',
            name='dynamic_content',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
