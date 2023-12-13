from django.db import models
from users.models import User

# Create your models here.
class Resume(models.Model):
    job_skills_choices = ( #New text field dropdown
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
    )

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

    location_choices = (
        ('Abra','Abra'),
        ('Agusan del Norte','Agusan del Norte'),
        ('Agusan del Sur','Agusan del Sur'),
        ('Aklan','Aklan'),
        ('Albay','Albay'),
        ('Antique','Antique'),
        ('Apayao','Apayao'),
        ('Aurora','Aurora'),
        ('Basilan','Basilan'),
        ('Bataan','Bataan'),
        ('Benguet','Benguet'),
        ('Biliran','Biliran'),
        ('Bohol','Bohol'),
        ('Bukidnon','Bukidnon'),
        ('Bulacan','Bulacan'),
        ('Cagayan','Cagayan'),
        ('Camarines Norte','Camarines Norte'),
        ('Camarines Sur','Camarines Sur'),
        ('Camiguin','Camiguin'),
        ('Capiz','Capiz'),
        ('Catanduanes','Catanduanes'),
        ('Cavite','Cavite'),
        ('Cebu','Cebu'),
        ('Cotabato','Cotabato'),
        ('Davao de Oro','Davao de Oro'),
        ('Davao del Norte','Davao del Norte'),
        ('Davao del Sur','Davao del Sur'),
        ('Davao Occidental','Davao Occidental'),
        ('Davao Oriental','Davao Oriental'),
        ('Dinagat Islands','Dinagat Islands'),
        ('Eastern Samar','Eastern Samar'),
        ('Guimaras','Guimaras'),
        ('Ifugao','Ifugao'),
        ('Ilocos Norte','Ilocos Norte'),
        ('Ilocos Sur','Ilocos Sur'),
        ('Iloilo','Iloilo'),
        ('Isabela','Isabela'),
        ('Kalinga','Kalinga'),
        ('La Union','La Union'),
        ('Laguna','Laguna'),
        ('Lanao del Norte','Lanao del Norte'),
        ('Lanao del Sur','Lanao del Sur'),
        ('Leyte','Leyte'),
        ('Maguindanao del Norte','Maguindanao del Norte'),
        ('Maguindanao del Sur','Maguindanao del Sur'),
        ('Marinduque','Marinduque'),
        ('Masbate','Masbate'),
        ('Misamis Occidental','Misamis Occidental'),
        ('Misamis Oriental','Misamis Oriental'),
        ('Mountain Province','Mountain Province'),
        ('Negros Occidental','Negros Occidental'),
        ('Negros Oriental','Negros Oriental'),
        ('Nothern Samar','Nothern Samar'),
        ('Nueva Ecija','Nueva Ecija'),
        ('Nueva Vizcaya','Nueva Vizcaya'),
        ('Occidental Mindoro','Occidental Mindoro'),
        ('Oriental Mindoro','Oriental Mindoro'),
        ('Palawan','Palawan'),
        ('Pampanga','Pampanga'),
        ('Pangasinan','Pangasinan'),
        ('Quezon','Quezon'),
        ('Quirino','Quirino'),
        ('Rizal','Rizal'),
        ('Romblon','Romblon'),
        ('Samar','Samar'),
        ('Sarangani','Sarangani'),
        ('Siquijor','Siquijor'),
        ('Sorsogon','Sorsogon'),
        ('South Cotabato','South Cotabato'),
        ('Southern Leyte','Southern Leyte'),
        ('Sultan Kudarat','Sultan Kudarat'),
        ('Sulu','Sulu'),
        ('Surigao del Norte','Surigao del Norte'),
        ('Surigao del Sur','Surigao del Sur'),
        ('Tarlac','Tarlac'),
        ('Tawi-tawi','Tawi-tawi'),
        ('Zambales','Zambales'),
        ('Zamboanga del Norte','Zamboanga del Norte'),
        ('Zamboanga del Sur','Zamboanga del Sur'),
        ('Zamboanga Sibugay','Zamboanga Sibugay'),
        ('Metro Manila','Metro Manila')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null = True, blank = True)
    surname = models.CharField(max_length=100, null = True, blank = True)
    location = models.CharField(max_length=100, choices=location_choices, null=True, blank=True)
    job_title = models.CharField(max_length=100,  choices=job_title_choices, null = True, blank = True)
    upload_resume = models.FileField(upload_to='resume', null=True, blank=True)
    job_skills =  models.CharField(max_length=20, choices=job_skills_choices, null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.surname}'
