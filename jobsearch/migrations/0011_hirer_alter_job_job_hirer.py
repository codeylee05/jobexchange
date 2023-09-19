# Generated by Django 4.2.4 on 2023-09-11 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0010_alter_job_job_hirer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hirer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hirer_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='job_hirer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hirer_jobs', to='jobsearch.hirer'),
        ),
    ]
