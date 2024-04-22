from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View, DeleteView
from app.models import *

class Indexview(TemplateView):
    template_name = 'privatesectors/index.html'

class AddVacancy(TemplateView):
    template_name = 'privatesectors/addvacancy.html'
    
    def post(self,request):
        swrk=priv_sect.objects.get(user_id=self.request.user.id)
        jobtitle = request.POST['jobtitle']
        experience = request.POST['experience']
        description = request.POST['description']
        qualification = request.POST['qualification']
               
        se = Vacancy()
        se.company_id = swrk.id
        se.jobtitle = jobtitle
        se.experience = experience
        se.description = description
        se.qualification = qualification
        se.status = "added"
        se.save()
        return render(request, 'privatesectors/index.html', {'message': "added successfull"})
    
class ViewVacancy(TemplateView):
    template_name = 'privatesectors/viewvacancy.html'
    def get_context_data(self, **kwargs):
        context = super(ViewVacancy,self).get_context_data(**kwargs)
        swrk=priv_sect.objects.get(user_id=self.request.user.id)
        ski = Vacancy.objects.filter(company_id=swrk.id)

        context['ski'] = ski
        return context
    
class ViewJobApplications(TemplateView):
    template_name = 'privatesectors/viewjobappli.html'
    def get_context_data(self, **kwargs):
        context = super(ViewJobApplications,self).get_context_data(**kwargs)
        swrk=priv_sect.objects.get(user_id=self.request.user.id)
        ski = JobApplication.objects.filter(vacancy__company_id=swrk.id)

        context['ski'] = ski
        return context
    
class Approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = JobApplication.objects.get(pk=id)
        user.status='approved'
        user.save()
        return render(request,'privatesectors/index.html',{'message':"Approved"})
    

class Reject(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = JobApplication.objects.get(pk=id)
        user.status='rejected'
        user.save()
        return render(request,'privatesectors/index.html',{'message':"Approved"})

class ScheduleInterview(TemplateView):
    template_name = 'privatesectors/interview_sch.html'
    def get_context_data(self, **kwargs):
        context = super(ScheduleInterview,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = JobApplication.objects.filter(id=id)

        context['ski'] = ski
        return context
    
    def post(self,request):
        date = request.POST['date']
        time = request.POST['time']
        description = request.POST['description']
        id=request.POST["id"]

        se = Interview()
        se.application_id = id
        se.date = date
        se.time = time
        se.description = description
        se.status = "scheduled"
        se.save()
        sa = JobApplication.objects.get(id=id)
        sa.status = "scheduled"
        sa.save()
        
        return render(request, 'privatesectors/index.html', {'message': "scheduled successfull"})

class ViewInterview(TemplateView):
    template_name = 'privatesectors/interview_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewInterview,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        swrk=priv_sect.objects.get(user_id=self.request.user.id)
        ski = Interview.objects.filter(application__vacancy__company_id=swrk.id,id=id)

        context['ski'] = ski
        return context

class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = "/privatesectors/ViewVacancy"
    template_name = "privatesectors/confirm_delete.html"