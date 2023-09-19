from django.contrib import admin
from .models import Job, Application


class JobInline(admin.TabularInline):

    model = Application

class JobAdmin(admin.ModelAdmin):

    list_display = ("id", "job_name", "job_level", "job_hirer", "job_salary", "job_location", "job_created_at", "job_description")
    inlines = [JobInline]

admin.site.register(Job, JobAdmin)


class ApplicationAdmin(admin.ModelAdmin):

    list_display = ("id", "target_job", "job_applicant", "application_created_at", "application_resume",)

admin.site.register(Application, ApplicationAdmin)
