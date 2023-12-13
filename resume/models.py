from django.db import models
from users.models import User

# Create your models here.
class Resume(models.Model):
    """job_skills_choices = ( #New text field dropdown
        ('Communication', 'Communication'),
        ('Computer', 'Computer'),
        ('Creative', 'Creative'),
        ('Management', 'Management'),
        ('Problem-solving', 'Problem-solving'),
        ('Orgnizational', 'Organizational'),
        ('Leadership', 'Leadership'),
        ('Interpersonal', 'Interpersonal'),
        ('Marketing', 'Marketing'),
        ('Technical', 'Technical') 
    )"""

    job_title_choices = ( 
        ('Account Executive', 'Account Executive'),
        ('Administrator', 'Administrator'),
        ('Architect', 'Architect'),
        ('Copywriter', 'Copywriter'),
        ('Customer Service Manager', 'Customer Service Manager'),
        ('Data Entry', 'Data Entry'),
        ('Engineer', 'Engineer'),
        ('Financial Planner', 'Financial Planner'),
        ('Project Manager', 'Project Manager'),
        ('Office Clerk', 'Office Clerk'),
        ('Python Web Developer', 'Python Web Developer') 
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null = True, blank = True)
    surname = models.CharField(max_length=100, null = True, blank = True)
    location = models.CharField(max_length=100, null = True, blank = True)
    job_title = models.CharField(max_length=100,  choices=job_title_choices, null = True, blank = True)
    upload_resume = models.FileField(upload_to='resume', null=True, blank=True)
    # job_skills =  models.CharField(max_length=20, choices=job_skills_choices, null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.surname}'
