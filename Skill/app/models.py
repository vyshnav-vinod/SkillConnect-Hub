from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)

class job_seeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)

class priv_sect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    licence = models.FileField(null=True)
    
class skilled_worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    
class job_type(models.Model):
   jobtype = models.CharField(max_length=50,null=True)

class skilled_worker_details(models.Model):
    sworker = models.ForeignKey(skilled_worker, on_delete=models.CASCADE,null=True)
    jobtype = models.CharField(max_length=50,null=True)
    experience = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)

class Services(models.Model):
    sworker = models.ForeignKey(skilled_worker_details, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    description = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=100,null=True)

class Vacancy(models.Model):
    company = models.ForeignKey(priv_sect, on_delete=models.CASCADE,null=True)
    jobtitle = models.CharField(max_length=50,null=True)
    experience = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    qualification = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)

class JobApplication(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(job_seeker, on_delete=models.CASCADE,null=True)
    experience = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    qualification = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    resume = models.FileField(null=True)

class Interview(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=200,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status = models.CharField(max_length=100,null=True)

class Training_Section(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True)
    video = models.FileField(null=True)
    status = models.CharField(max_length=100,null=True)

class Feedback(models.Model):
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,null=True)
    feedback=models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=100, null=True)
    action = models.CharField(max_length=50, null=True)
