# Generated by Django 4.2.4 on 2023-09-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0011_hirer_alter_job_job_hirer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_hirer',
            field=models.CharField(max_length=32),
        ),
    ]
