# Generated by Django 5.0.7 on 2024-08-30 12:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0007_alter_channelmodel_createdfrom_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='emoji_check',
            field=models.ManyToManyField(blank=True, related_name='emoji_check', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='emoji_handsup',
            field=models.ManyToManyField(blank=True, related_name='emoji_handsup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='emoji_nerd',
            field=models.ManyToManyField(blank=True, related_name='emoji_nerd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='emoji_rocket',
            field=models.ManyToManyField(blank=True, related_name='emoji_rocket', to=settings.AUTH_USER_MODEL),
        ),
    ]
