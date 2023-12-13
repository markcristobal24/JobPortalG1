from django.shortcuts import render, redirect
from .models import ActivityLog
from django.contrib import messages
from users.models import User
from job.models import Job
from resume.models import Resume
from company.models import Company
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound


# Create your views here.
def manage_applicants(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'admin/manage_applicants.html', {'users':users})
    elif request.user.is_authenticated:
        return redirect('dashboard')

def manage_recruiters(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'admin/manage_recruiters.html', {'users':users})
    elif request.user.is_authenticated:
        return redirect('dashboard')

def manage_reports(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = User.objects.all()
        applicant_count = 0
        recruiter_count = 0
        for user in users:
            if user.is_applicant:
                applicant_count += 1
            elif user.is_recruiter:
                recruiter_count += 1

        jobs = Job.objects.all()
        job_count = 0
        for job in jobs:
            job_count+=1

        logs = ActivityLog.objects.all()

        companies = Company.objects.all()

        return render(request, 'admin/manage_reports.html', {
            'applicants':applicant_count, 
            'recruiters':recruiter_count, 
            'jobs':job_count,
            'logs':logs,
            'userlist':users,
            'joblist':jobs,
            'companylist':companies
            })
    elif request.user.is_authenticated:
        return redirect('dashboard')

def admin_jobs(request):
    if request.user.is_authenticated and request.user.is_superuser:
        jobs = Job.objects.all()
        return render(request, 'admin/manage_jobs.html', {'jobs':jobs})
    elif request.user.is_authenticated:
        return redirect('dashboard')

def activate_user(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User activated successfully')

        if user.is_applicant:
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin activated applicant {user.username}"
            )
            return redirect('manage-applicants')
        elif user.is_recruiter:
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin acivated recruiter {user.username}"
            )
            return redirect('manage-recruiters')
    elif request.user.is_authenticated:
        return redirect('dashboard')

def deactivate_user(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User deactivated successfully')
        if user.is_applicant:
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin deacivated applicant {user.username}"
            )
            return redirect('manage-applicants')
        elif user.is_recruiter:
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin deacivated recruiter {user.username}"
            )
            return redirect('manage-recruiters')
    elif request.user.is_authenticated:
        return redirect('dashboard')

def edit_user(request, user_id):
    pass

def view_resume(request, user_id):
    if request.user.is_authenticated:
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
    elif request.user.is_authenticated:
        return redirect('dashboard')

def activate_job(request, job_id):
    if request.user.is_authenticated and request.user.is_superuser:
        job = Job.objects.get(pk=job_id)
        job.is_available = True
        job.save()
        messages.add_message(request, messages.SUCCESS, 'Job activated successfully')
        ActivityLog.objects.create(
            user="Admin",
            details=f"Admin acivated job {job_id}"
        )
        return redirect('admin-jobs')
    elif request.user.is_authenticated:
        return redirect('dashboard')

def deactivate_job(request, job_id):
    if request.user.is_authenticated and request.user.is_superuser:
        job = Job.objects.get(pk=job_id)
        job.is_available = False
        job.save()
        messages.add_message(request, messages.SUCCESS, 'Job deactivated successfully')
        ActivityLog.objects.create(
            user="Admin",
            details=f"Admin acivated job {job_id}"
        )
        return redirect('admin-jobs')
    elif request.user.is_authenticated:
        return redirect('dashboard')

def edit_user(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(pk=user_id)
        if request.method == 'GET':
            user.username = request.GET.get(f"username{user_id}")
            user.email = request.GET.get(f"email{user_id}")
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Updated user successfully')
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin edited User {user_id}"
            )
            if user.is_applicant:
                return redirect('manage-applicants')
            elif user.is_recruiter:
                return redirect('manage-recruiters')
    elif request.user.is_authenticated:
        return redirect('dashboard')
    
def edit_job(request, job_id):
    if request.user.is_authenticated and request.user.is_superuser:
        job = Job.objects.get(pk=job_id)
        if request.method == 'GET':
            job.company.name = request.GET.get(f"company_name{job_id}")
            job.title = request.GET.get(f"job_title{job_id}")
            job.save()
            messages.add_message(request, messages.SUCCESS, 'Updated job successfully')
            ActivityLog.objects.create(
                user="Admin",
                details=f"Admin edited Job {job_id}"
            )

            return redirect('admin-jobs')

    elif request.user.is_authenticated:
        return redirect('dashboard')

def delete_user(request, user_id):
    if request.user.is_authenticated and request.user.is_superuser:
        user = User.objects.get(pk=user_id)
        if user.is_applicant:
            user.delete()
            return redirect('manage-applicants')
        elif user.is_recruiter:
            user.delete()
            return redirect('manage-recruiters')
    elif request.user.is_authenticated:
        return redirect('dashboard')
    
def delete_job(request, job_id):
    if request.user.is_authenticated and request.user.is_superuser:
        job = Job.objects.get(pk=job_id)
        job.delete()
        return redirect('admin-jobs')
    elif request.user.is_authenticated:
        return redirect('dashboard')