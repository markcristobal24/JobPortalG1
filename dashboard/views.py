from django.shortcuts import render, redirect
from admin2.models import ActivityLog
from users.models import User
from job.models import Job

def dashboard(request):
    logs = ActivityLog.objects.all()

    users = User.objects.all()
    total_applicants = 0
    active_applicants = 0
    total_recruiters = 0
    active_companies = 0
    total_jobs = 0
    available_jobs = 0

    for user in users:
        if user.is_applicant:
            total_applicants += 1
            if user.is_active:
                active_applicants += 1
                print(f"Active applicant: {user.email}")
        elif user.is_recruiter:
            total_recruiters += 1
            if user.has_company:
                active_companies += 1
                print(f"Active companies: {user.email}")

    jobs = Job.objects.all()
    for job in jobs:
        total_jobs += 1
        if job.is_available:
            available_jobs += 1

    return render(request, 'dashboard/dashboard.html', 
                  {'total_applicants':total_applicants,
                   'active_applicants':active_applicants,
                   'total_recruiters':total_recruiters,
                   'active_companies':active_companies,
                   'total_jobs':total_jobs,
                   'available_jobs':available_jobs,
                   'logs':logs})