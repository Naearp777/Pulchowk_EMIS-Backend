# Generated by Django 4.0 on 2022-02-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0004_remove_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
