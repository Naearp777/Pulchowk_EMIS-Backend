# Generated by Django 4.0 on 2022-02-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0007_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='excel')),
            ],
        ),
    ]