from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from users.models import User
from admin2.models import ActivityLog

@login_required
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New job has been created')
                applicant_emails = User.objects.filter(is_applicant=True).values_list('email', flat=True)
                for email in applicant_emails:
                    send_mail('Jobbl: New Job Alert', '<company> has posted a new job listing. Check it out!', 'jobbl.jobalerts@gmail.com', [email], fail_silently=False)
                
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')

@login_required
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your form job is updated')
            
            ActivityLog.objects.create(
                user=f"User {job.user_id}",
                details=f"User {job.user_id} updated {job.title}"
            )
            
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form':form}
        return render(request, 'job/update_job.html', context)
    
def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)

def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission Denied')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have successfully applied! Please see dashboard')
            
            ActivityLog.objects.create(
                user=f"User {request.user.id}",
                details=f"User {request.user.id} applied to Job {job.id}"
            )
            
            return redirect('dashboard')
    else:
        messages.info(request, 'Please login to continue')
        return redirect('login')
    
def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job, 'applicants':applicants}
    return render(request, 'job/all_applicants.html', context)

def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request, 'job/applied_job.html', context)

def delete_job(request, pk):
    delete_job = get_object_or_404(Job, pk=pk)
    try:
        delete_job.delete()
        messages.success(request, 'Job successfully removed.')
        return redirect('manage-jobs')
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('manage-jobs')