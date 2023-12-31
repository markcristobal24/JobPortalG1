from django.urls import path
from . import views
from .views import applicant_change_profile

urlpatterns = [
    path('register-applicant/', views.register_applicant, name='register-applicant'),
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('applicant-profile/', views.applicant_profile, name='applicant-profile'),
    path('applicant-change-pass/', views.applicant_change_pass, name='applicant-change-pass'),

    path('delete-account', views.delete_account, name='delete-account'),

    path('recruit-change-pass/', views.recruit_change_pass, name='recruit-change-pass'),
    path('recruit-change-profile/', views.recruit_change_profile, name='recruit-change-profile'),
    
    path('applicant-change-profile/<int:user_id>/', applicant_change_profile, name='applicant-change-profile')


]