# Generated by Django 3.2.5 on 2022-02-12 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_info',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customuser.user'),
            preserve_default=False,
        ),
    ]
