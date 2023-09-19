from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Job, Application

missing_validator = "Fill in all required fields and resubmit"
login_validator = "Credentials incorrect. Try again"
register_validator = "Enter the correct information (Amount bigger than 0 and correct level).Try again"

def index(request):

    return render(request, "jobsearch/index.html")


def search(request):

    return render(request, "jobsearch/search.html")


def process_search(request):

    if request.method == "POST":

        search_name = request.POST["name"].lower()
        search_level = request.POST["level"].upper()
        search_location = request.POST["location"].lower()

        jobs = Job.objects.filter(job_name=search_name, job_level=search_level, job_location=search_location)
        if search_name and search_level and search_location != "":

            return render(request, "jobsearch/result.html", {
                "name": search_name,
                "level": search_level,
                "location": search_location,
                "jobs": jobs
            })

        else:

            return render(request, "jobsearch/search.html", {
                "message": missing_validator
            })

    else:

        return redirect("search")


@login_required
def register(request):

    return render(request, "jobsearch/register.html")

'''Issue in following function: A job is being saved even though the .save is not called due to invalidity'''
def process_register(request):

    if request.method == "POST":

        reg_hirer = request.POST["hirer"].lower()
        reg_name = request.POST["name"].lower()
        reg_level = request.POST["level"].upper()
        reg_location = request.POST["location"].lower()
        reg_salary = int(request.POST["salary"])
        reg_description = request.POST["description"]

        new_job = Job.objects.create(job_name=reg_name, job_level=reg_level, job_hirer=reg_hirer, job_location=reg_location, job_salary=reg_salary, job_description=reg_description)
        if not new_job.is_valid_job():
            
            return render(request, "jobsearch/register.html", {
                "message": register_validator
            })
        else:

            new_job.save()
                
            return HttpResponse("<h1>Job created successfully!</div>")

    else:

        return redirect("register")


@login_required
def apply(request, job_id):

    job = Job.objects.get(id=job_id)
    return render(request, "jobsearch/apply.html", {
        "job": job
    })


def process_apply(request, job_id):

    if request.method == "POST":

        '''applicant_name = request.POST["name"]
        applicant_surname = request.POST["surname"]
        applicant_email = request.POST["email"]
        applicant_resume = request.POST["resume"]''' #The input values are not necessary to create a new application object, just the request.user

        user = request.user
        job = Job.objects.get(id=job_id)

        application = Application(target_job=job, job_applicant=user)
        application.save()

        return HttpResponse("<h1>Job applied for successfully!</div>")

    else:
        
        return redirect("index")


@login_required
def applied_jobs(request):

    user = request.user
    user_applications = Application.objects.filter(job_applicant=user.id)

    return render(request, "jobsearch/applied_jobs.html", {
        "applications": user_applications
    })


@login_required
def delete_application(request, application_id):

    user_application = Application.objects.filter(id=application_id)

    user_application.delete()

    return HttpResponse(f"<h1>Your job application has been deleted!<h1>")


def user_login(request):

    if request.method == "POST":

        user_username = request.POST["username"]
        user_password = request.POST["password"]

        user = authenticate(username=user_username, password=user_password) 
        if user is not None:

            login(request, user)

            return HttpResponseRedirect(reverse("index"))
        
        else:

            return render(request, "jobsearch/login.html", {
                "message": login_validator
            })
       
    else:

       return render(request, "jobsearch/login.html")


def explore_jobs(request):

    all_jobs = Job.objects.all()

    context = {"jobs": all_jobs}

    return render(request, "jobsearch/explore.html", context)


@login_required
def user_view(request):

    return render(request, "jobsearch/user.html")

