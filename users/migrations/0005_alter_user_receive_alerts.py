



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_receive_alerts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='receive_alerts',
            field=models.BooleanField(default=True),
        ),
    ]
