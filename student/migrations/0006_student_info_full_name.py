# Generated by Django 3.2.5 on 2022-02-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_info_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
