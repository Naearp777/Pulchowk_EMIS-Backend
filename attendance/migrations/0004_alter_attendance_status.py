# Generated by Django 3.2.5 on 2022-03-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
