# Generated by Django 4.0 on 2022-02-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
