# Generated by Django 4.0 on 2022-02-10 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='name',
        ),
    ]
