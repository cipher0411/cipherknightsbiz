# Generated by Django 5.0.6 on 2024-06-15 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_dev', '0005_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Demo',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
