# Generated by Django 4.2.15 on 2024-09-10 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0014_generatelearningcontentcontainer_is_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
    ]