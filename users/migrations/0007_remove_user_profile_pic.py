# Generated by Django 4.2.7 on 2023-12-13 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
