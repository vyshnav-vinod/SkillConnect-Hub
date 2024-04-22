
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from app.models import *

class Indexview(TemplateView):
    template_name = 'jobseeker/index.html'

    def get_context_data(self, **kwargs):
        context = super(Indexview,self).get_context_data(**kwargs)

        ski = Vacancy.objects.all()

        context['ski'] = ski
        return context
    
    def post(self, request, *args, **kwargs):
        job = request.POST['job']
        host = Vacancy.objects.filter(jobtitle__icontains=job)
        return render(request, 'jobseeker/index.html', {'ski':host})
    
class AddApplication(TemplateView):
    template_name = 'jobseeker/applyjob.html'
    def get_context_data(self, **kwargs):
        context = super(AddApplication,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = Vacancy.objects.filter(id=id)

        context['ski'] = ski
        return context
    
    def post(self,request):
        swrk=job_seeker.objects.get(user_id=self.request.user.id)
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        description = request.POST['description']
        resume=request.FILES['resume']
        fii=FileSystemStorage()
        filesss=fii.save(resume.name,resume)
        id=request.POST["id"]

        se = JobApplication()
        se.user_id = swrk.id
        se.vacancy_id = id
        se.experience = experience
        se.description = description
        se.qualification = qualification
        se.resume = filesss
        se.status = "applied"
        se.save()
        return render(request, 'jobseeker/index.html', {'message': "added successfull"})
    
class ViewJobApplications(TemplateView):
    template_name = 'jobseeker/viewjobappli.html'
    def get_context_data(self, **kwargs):
        context = super(ViewJobApplications,self).get_context_data(**kwargs)
        swrk=job_seeker.objects.get(user_id=self.request.user.id)
        ski = JobApplication.objects.filter(user_id=swrk.id)

        context['ski'] = ski
        return context

class ViewInterview(TemplateView):
    template_name = 'jobseeker/interview_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewInterview,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        swrk=job_seeker.objects.get(user_id=self.request.user.id)
        ski = Interview.objects.filter(application__user_id=swrk.id,id=id)

        context['ski'] = ski
        return context
    
class ViewCategory(TemplateView):
    template_name = 'jobseeker/training_cat.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCategory,self).get_context_data(**kwargs)
        ski = Training_Section.objects.all()

        context['ski'] = ski
        return context
    
class ViewTrainingSec(TemplateView):
    template_name = 'jobseeker/viewtrainingsec.html'
    def get_context_data(self, **kwargs):
        context = super(ViewTrainingSec,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = Training_Section.objects.filter(id=id)

        context['ski'] = ski
        return context
    
class TrainingSecDetails(TemplateView):
    template_name = 'jobseeker/trainingsession.html'
    def get_context_data(self, **kwargs):
        context = super(TrainingSecDetails,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = Training_Section.objects.filter(id=id)

        context['ski'] = ski
        return context