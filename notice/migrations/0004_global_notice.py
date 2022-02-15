# Generated by Django 3.2.5 on 2022-02-15 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0003_alter_notice_publish_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='global_notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(blank=True, upload_to='notice/files/')),
                ('publish_by', models.CharField(max_length=100)),
                ('publish_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Global Notices',
            },
        ),
    ]