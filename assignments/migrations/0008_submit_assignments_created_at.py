# Generated by Django 3.2.5 on 2022-02-28 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0007_submit_assignments_marked'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit_assignments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
