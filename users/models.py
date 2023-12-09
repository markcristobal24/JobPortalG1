from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    has_resume = models.BooleanField(default = False)
    has_company = models.BooleanField(default = False)

