# Generated by Django 3.2.5 on 2022-02-13 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_materials', '0003_auto_20220213_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='materials',
        ),
        migrations.AlterField(
            model_name='materials',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_materials.folder'),
        ),
    ]
