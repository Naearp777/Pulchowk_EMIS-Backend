# Generated by Django 3.2.5 on 2022-03-02 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0005_departmentadmin_info'),
        ('assignments', '0008_submit_assignments_created_at'),
        ('classes', '0004_auto_20220214_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(null=True, upload_to='notice/files/')),
                ('publish_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publish_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
            ],
            options={
                'verbose_name_plural': 'Notices',
            },
        ),
        migrations.CreateModel(
            name='Global_Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(null=True, upload_to='notice/files/')),
                ('publish_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publish_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Global Notices',
            },
        ),
        migrations.CreateModel(
            name='Department_Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(null=True, upload_to='notice/files/')),
                ('publish_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publish_by_dept', to=settings.AUTH_USER_MODEL)),
                ('publish_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'verbose_name_plural': 'Department Notices',
            },
        ),
        migrations.CreateModel(
            name='Assignmentnotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.give_assignments')),
                ('publish_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publish_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
            ],
            options={
                'verbose_name_plural': 'Notices',
            },
        ),
    ]
