# Generated by Django 4.0 on 2022-02-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0008_excelfileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_changed',
            field=models.BooleanField(default=False),
        ),
    ]
