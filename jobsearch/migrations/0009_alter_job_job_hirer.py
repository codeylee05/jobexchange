# Generated by Django 4.2.4 on 2023-09-11 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobsearch', '0008_application_application_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_hirer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]