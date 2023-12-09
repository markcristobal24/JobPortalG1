from django.shortcuts import render, redirect
from .models import Admin2
from django.contrib import messages
from users.models import User
from job.models import Job
from resume.models import Resume
from django.http import FileResponse


# Create your views here.
def manage_applicants(request):
    users = User.objects.all()
    return render(request, 'admin/manage_applicants.html', {'users':users})

def manage_recruiters(request):
    users = User.objects.all()
    return render(request, 'admin/manage_recruiters.html', {'users':users})

def admin_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'admin/manage_jobs.html', {'jobs':jobs})

def activate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User activated successfully')
    if user.is_applicant:
        return redirect('manage-applicants')
    elif user.is_recruiter:
        return redirect('manage-recruiters')

def deactivate_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User deactivated successfully')
    if user.is_applicant:
        return redirect('manage-applicants')
    elif user.is_recruiter:
        return redirect('manage-recruiters')

def edit_user(request, user_id):
    pass

def view_resume(request, user_id):
    file_path = "media/resume/IT_403_WMAD_-_Project_Rubric_Job_Portal_-_1st_Sem_22-23.pdf"
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    return response

def activate_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.is_available = True
    job.save()
    messages.add_message(request, messages.SUCCESS, 'Job activated successfully')
    return redirect('admin-jobs')

def deactivate_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.is_available = False
    job.save()
    messages.add_message(request, messages.SUCCESS, 'Job deactivated successfully')
    return redirect('admin-jobs')