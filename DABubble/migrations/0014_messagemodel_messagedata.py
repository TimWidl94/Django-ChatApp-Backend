# Generated by Django 5.0.7 on 2024-09-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0013_rename_thread_channel_id_threadmessagemodel_thread_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='messageData',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]