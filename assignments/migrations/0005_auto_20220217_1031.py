# Generated by Django 3.2.5 on 2022-02-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_remove_give_assignments_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='give_assignments',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submit_assignments',
            name='obtain_points',
            field=models.IntegerField(default=0),
        ),
    ]
