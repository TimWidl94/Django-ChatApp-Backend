# Generated by Django 5.0.7 on 2024-08-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0012_privatemessagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatechannelmodel',
            name='channelPartner',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
