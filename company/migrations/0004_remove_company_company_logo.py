# Generated by Django 4.2.7 on 2023-12-13 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_logo',
        ),
    ]