# Generated by Django 5.0.6 on 2024-06-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_dev', '0008_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='otp_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]