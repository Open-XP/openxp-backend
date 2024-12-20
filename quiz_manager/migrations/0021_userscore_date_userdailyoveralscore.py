# Generated by Django 4.2.13 on 2024-07-20 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_manager', '0020_alter_totalstudytime_id_alter_useranswer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='UserDailyOveralScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('total_score', models.IntegerField(default=0)),
                ('total_correct', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
