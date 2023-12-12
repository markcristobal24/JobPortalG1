from django.shortcuts import render, redirect
from .models import Admin2
from django.contrib import messages
from users.models import User
from job.models import Job
from resume.models import Resume
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound


# Create your views here.
def manage_applicants(request):
    users = User.objects.all()
    return render(request, 'admin/manage_applicants.html', {'users':users})

def manage_recruiters(request):
    users = User.objects.all()
    return render(request, 'admin/manage_recruiters.html', {'users':users})

def manage_reports(request):
    users = User.objects.all()
    applicant_count = 0
    recruiter_count = 0
    for user in users:
        if user.is_applicant:
            applicant_count += 1
            print("Applicant: ",user.email)
        elif user.is_recruiter:
            recruiter_count += 1
            print("Recruiter: ",user.email)

    jobs = Job.objects.all()
    job_count = 0
    for job in jobs:
        job_count+=1
    return render(request, 'admin/manage_reports.html', {'applicants':applicant_count, 'recruiters':recruiter_count, 'jobs':job_count})

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
    try:
        print("id: ",user_id)
        resume = get_object_or_404(Resume, user=user_id)

        if resume.upload_resume:
            file_path = str(resume.upload_resume.path)
            
            response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="resume.pdf"'
            return response
        else:
            raise Http404("No resume file available for this user.")
    except Http404 as e:
        return HttpResponseNotFound(f"Resume not found: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return HttpResponse("An error occurred", status=500)

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