# Generated by Django 4.0.3 on 2022-04-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_rename_nickname_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
