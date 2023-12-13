from django.urls import path
from . import views
from .views import activate_user, deactivate_user, edit_user, activate_job, deactivate_job,view_resume, edit_job, delete_user, delete_job


urlpatterns = [
    path('manage-applicants/', views.manage_applicants, name='manage-applicants'),
    path('manage-recruiters/', views.manage_recruiters, name='manage-recruiters'),
    path('admin-jobs/', views.admin_jobs, name='admin-jobs'),
    path('manage-reports/', views.manage_reports, name='manage-reports'),
    path('activate_user/<int:user_id>/', activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', deactivate_user, name='deactivate_user'),
    path('view_resume/<int:user_id>/', view_resume, name='view_resume'),
    path('activate_job/<int:job_id>/', activate_job, name='activate_job'),
    path('deactivate_job/<int:job_id>/', deactivate_job, name='deactivate_job'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('edit_job/<int:job_id>/', edit_job, name='edit_job'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete_job/<int:job_id>/', delete_job, name='delete_job')

]