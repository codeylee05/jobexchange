# Generated by Django 4.2.4 on 2023-09-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_level',
            field=models.CharField(choices=[('ENTRY', 'ENTRY'), ('JUNIOR', 'JUNIOR'), ('SENIOR', 'SENIOR')], max_length=6),
        ),
    ]
