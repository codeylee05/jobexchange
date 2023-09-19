from django.db import models
from django.contrib.auth.models import User

ENTRY = "ENTRY" #I used the full name for database population to make things easier on the client side
JUNIOR = "JUNIOR"
SENIOR = "SENIOR"

JOB_LEVELS = [
    (ENTRY, "ENTRY"),
    (JUNIOR, "JUNIOR"),
    (SENIOR, "SENIOR"),
]

#for validation function purposes:
valid_job_levels = ["ENTRY", "JUNIOR", "SENIOR"]

class Job(models.Model):

    job_name = models.CharField(max_length=32)
    job_level = models.CharField(max_length=6, choices=JOB_LEVELS)
    job_hirer = models.CharField(max_length=32)
    job_location = models.CharField(max_length=32)
    job_salary = models.IntegerField()
    job_created_at = models.DateField(auto_now=True)
    job_description = models.TextField(null=True)

    def is_valid_job(self): #

        return self.job_name and self.job_level and self.job_hirer and self.job_location and self.job_description != "" and self.job_salary > 0 and self.job_level in valid_job_levels


class Application(models.Model):

    target_job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="appplications_to_job")
    job_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_applications", default=1)
    application_created_at = models.DateField(auto_now=True)
    application_resume = models.FileField(upload_to="application_resumes/", max_length=100, default="defaults/default_resume.txt")

    def is_valid_application(self):

        return self.target_job and self.job_applicant != ""