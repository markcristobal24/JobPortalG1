from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout, update_session_auth_hash
from .models import User
from .form import RegisterUserForm, ChangePasswordForm
from company.form import EditCompanyForm
from resume.models import Resume
from company.models import Company
from django.contrib.auth.decorators import login_required
from admin2.models import ActivityLog

# Create your views here.
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created.')
            
            ActivityLog.objects.create(
                user=f"User {var.id}",
                details=f"User {var.id} created an applicant account"
            )

            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            print(form.errors)
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_applicant.html', context)

def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created.')
            
            ActivityLog.objects.create(
                user=f"User {var.id}",
                details=f"User {var.id} created a recruiter account"
            )
            
            return redirect('login')

        else:
            messages.warning(request, 'Something went wrong')
            print(form.errors)
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_recruiter.html', context)

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email, password=password)
        if user is not None and user.is_active:
            login(request, user)

            if user.is_superuser is not True:
                ActivityLog.objects.create(
                    user=f"User {user.id}",
                    details=f"User {user.id} logged in"
                )

            return redirect('dashboard')
        elif user is None:
            messages.warning(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended.')
    
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
                #return redirect here
            
            if not request.user.check_password(current_password):
                messages.error(request, "Current password is incorrect.")
                #return redirect here
            
            request.user.set_password(new_password)
            request.user.save()

            update_session_auth_hash(request, request.user)

            messages.success(request, "Password successfully changed.")
            #return redirect here
        else:
            form = ChangePasswordForm()
        #return render here

#new function sa may applicant
def applicant_profile(request):
    
    return render(request, 'users/applicant_profile.html')   

def applicant_change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            if new_password != confirm_password:
                messages.warning(request, "New passwords do not match.")
                #return redirect here
            
            elif not request.user.check_password(current_password):
                messages.warning(request, "Current password is incorrect.")
                #return redirect here
            else:
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)

                messages.success(request, "Password successfully changed.")
                return redirect('dashboard')
        else:
            form = ChangePasswordForm()
    form = ChangePasswordForm()
    return render(request, 'users/applicant_change_pass.html', {'form': form})         
  

def recruit_change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            if new_password != confirm_password:
                messages.warning(request, "New passwords do not match.")
                #return redirect here
            
            elif not request.user.check_password(current_password):
                messages.warning(request, "Current password is incorrect.")
                #return redirect here
            else:
                request.user.set_password(new_password)
                request.user.save()

                update_session_auth_hash(request, request.user)

                messages.success(request, "Password successfully changed.")
                return redirect('dashboard')
        else:
            form = ChangePasswordForm()
    form = ChangePasswordForm()
    return render(request, 'company/recruit_change_pass.html', {'form': form})      


def recruit_change_profile(request):
    company = Company.objects.get(user=request.user)
    form = EditCompanyForm(instance=company)
    context = {'form':form}
    return render(request, 'company/recruit_change_profile.html', context) 


            

@login_required
def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()

        return redirect('login')
    return redirect('login')
