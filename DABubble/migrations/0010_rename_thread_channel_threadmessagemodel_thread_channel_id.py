# Generated by Django 5.0.7 on 2024-09-07 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0009_threadmessagemodel_emoji_check_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threadmessagemodel',
            old_name='thread_channel',
            new_name='thread_channel_id',
        ),
    ]
