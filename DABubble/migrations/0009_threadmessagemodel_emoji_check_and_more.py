# Generated by Django 5.0.7 on 2024-09-04 03:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0008_messagemodel_emoji_check_messagemodel_emoji_handsup_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='threadmessagemodel',
            name='emoji_check',
            field=models.ManyToManyField(blank=True, related_name='emoji_check_thread', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadmessagemodel',
            name='emoji_handsup',
            field=models.ManyToManyField(blank=True, related_name='emoji_handsup_thread', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadmessagemodel',
            name='emoji_nerd',
            field=models.ManyToManyField(blank=True, related_name='emoji_nerd_thread', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadmessagemodel',
            name='emoji_rocket',
            field=models.ManyToManyField(blank=True, related_name='emoji_rocket_thread', to=settings.AUTH_USER_MODEL),
        ),
    ]
