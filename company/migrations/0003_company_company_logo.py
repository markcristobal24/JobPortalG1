# Generated by Django 4.2.7 on 2023-12-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.FileField(blank=True, null=True, upload_to='company'),
        ),
    ]
