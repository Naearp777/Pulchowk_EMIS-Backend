# Generated by Django 4.0 on 2022-02-02 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='department',
        ),
    ]