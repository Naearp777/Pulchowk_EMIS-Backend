# Generated by Django 4.0 on 2022-02-10 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0003_rename_department_name_department_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'verbose_name_plural': 'Teachers_info',
            },
        ),
    ]