# Generated by Django 4.2.7 on 2023-12-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0003_remove_activitylog_activity_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=255)),
            ],
        ),
    ]