# Generated by Django 4.2.4 on 2023-09-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0002_alter_job_job_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
