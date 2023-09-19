# Generated by Django 4.2.4 on 2023-09-10 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobsearch', '0006_alter_job_job_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_created_at', models.DateField(auto_now=True)),
                ('job_applicant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_applications', to=settings.AUTH_USER_MODEL)),
                ('target_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='jobsearch.job')),
            ],
        ),
    ]
