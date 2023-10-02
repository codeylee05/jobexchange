from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("result/", views.process_search, name="process_search"),
    path("register/", views.register, name="register"),
    path("process-register/", views.process_register, name="process_register"),
    path("job<int:job_id>/apply/", views.apply, name="apply"),
    path("job<int:job_id>/process-apply/", views.process_apply, name="process_apply"),
    path("applied-jobs/", views.applied_jobs, name="applied_jobs"),
    path("delete-application/<int:application_id>/", views.delete_application, name="delete_application"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("explore/", views.explore_jobs, name="explore"),
    path("user/", views.user_view, name="user"),
]