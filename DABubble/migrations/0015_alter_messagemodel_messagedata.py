# Generated by Django 5.0.7 on 2024-09-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DABubble', '0014_messagemodel_messagedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='messageData',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
