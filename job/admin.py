from django.contrib import admin
from job.models import Job, ApplyJob, State, Industry

admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(State)
admin.site.register(Industry)

# Register your models here.
