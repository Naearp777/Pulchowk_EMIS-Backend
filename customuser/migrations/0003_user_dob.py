# Generated by Django 4.0 on 2022-01-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_rename_username_user_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
