# Generated by Django 5.0.7 on 2024-08-28 05:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0005_alter_avatarmodel_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelName', models.CharField(max_length=250)),
                ('channelDescription', models.CharField(max_length=250)),
                ('createdFrom', models.CharField(max_length=250)),
                ('privateChannel', models.BooleanField(default=False)),
                ('channelMembers', models.ManyToManyField(related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('threadOpen', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='DABubble.channelmodel')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadChannelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threadName', models.CharField(max_length=250)),
                ('threadDescription', models.CharField(max_length=250)),
                ('createdFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mainChannel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_channels', to='DABubble.channelmodel')),
                ('original_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='DABubble.messagemodel')),
                ('threadMember', models.ManyToManyField(related_name='thread_channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='thread_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thread_messages', to='DABubble.threadchannelmodel'),
        ),
        migrations.CreateModel(
            name='ThreadMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('thread_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='DABubble.threadchannelmodel')),
            ],
        ),
    ]
