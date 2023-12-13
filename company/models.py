from django.db import models
from users.models import User
# Create your models here.

class Company(models.Model):
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
    contact_person = models.CharField(max_length=255, null = True, blank = True)
    name = models.CharField(max_length=100, null = True, blank = True)
    est_date = models.PositiveIntegerField(null = True, blank = True)
    city = models.CharField(max_length=100, choices=location_choices,null = True, blank = True)
    state = models.CharField(max_length=100,  null=True, blank=True)
    company_logo = models.FileField(upload_to="company", null=True, blank=True)

    def __str__(self):
        return self.name