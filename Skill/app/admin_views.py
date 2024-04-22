from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import *
from app.models import *

from django.core.files.storage import FileSystemStorage

class Indexview(TemplateView):
    template_name = 'admin/index.html'
    
class jobtype(TemplateView):
    template_name = 'admin/jobtype.html'
    
    def post(self,request):
        jobtype = request.POST['job_type']
               
        se = job_type()
        se.jobtype = jobtype
        se.save()
        return render(request, 'admin/index.html', {'message': "added successfull"})
        
class user_verify(TemplateView):
    template_name = 'admin/jobseekerverify.html'
    def get_context_data(self, **kwargs):
        context = super(user_verify,self).get_context_data(**kwargs)

        user = job_seeker.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = user
        return context

class user_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class user_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})
    
class jobseeker_view(TemplateView):
    template_name = 'admin/jobseekeraproveview.html'
    def get_context_data(self, **kwargs):
        context = super(jobseeker_view,self).get_context_data(**kwargs)

        user = job_seeker.objects.filter(user__last_name='1',user__is_active='1')

        context['user'] = user
        return context
    
class privsect_verify(TemplateView):
    template_name = 'admin/privsectverify.html'
    def get_context_data(self, **kwargs):
        context = super(privsect_verify,self).get_context_data(**kwargs)

        user = priv_sect.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = user
        return context

class privsect_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class privsect_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})
    
class privsect_view(TemplateView):
    template_name = 'admin/privsectaproveview.html'
    def get_context_data(self, **kwargs):
        context = super(privsect_view,self).get_context_data(**kwargs)

        user = priv_sect.objects.filter(user__last_name='1',user__is_active='1')

        context['user'] = user
        return context
    
class skillwrkr_verify(TemplateView):
    template_name = 'admin/skilledworkerverify.html'
    def get_context_data(self, **kwargs):
        context = super(skillwrkr_verify,self).get_context_data(**kwargs)

        user = skilled_worker.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = user
        return context

class skillwrkr_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class skillwrkr_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})
    
class skillwrkr_view(TemplateView):
    template_name = 'admin/skilledworkeraproveview.html'
    def get_context_data(self, **kwargs):
        context = super(skillwrkr_view,self).get_context_data(**kwargs)

        user = skilled_worker.objects.filter(user__last_name='1',user__is_active='1')

        context['user'] = user
        return context
    
class ViewBookings(TemplateView):
    template_name = 'admin/viewbookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBookings,self).get_context_data(**kwargs)
        
        ski = Services.objects.all()

        context['ski'] = ski
        return context
    
class ViewJobApplications(TemplateView):
    template_name = 'admin/viewjobappli.html'
    def get_context_data(self, **kwargs):
        context = super(ViewJobApplications,self).get_context_data(**kwargs)
        
        ski = JobApplication.objects.all()

        context['ski'] = ski
        return context

class ViewInterview(TemplateView):
    template_name = 'admin/interview_details.html'
    def get_context_data(self, **kwargs):
        context = super(ViewInterview,self).get_context_data(**kwargs)
        # id=self.request.GET["id"]
        # swrk=priv_sect.objects.get(user_id=self.request.user.id)
        ski = Interview.objects.all()

        context['ski'] = ski
        return context

class ViewVacancy(TemplateView):
    template_name = 'admin/viewvacancy.html'
    def get_context_data(self, **kwargs):
        context = super(ViewVacancy,self).get_context_data(**kwargs)
        ski = Vacancy.objects.all()

        context['ski'] = ski
        return context

class jobtype(TemplateView):
    template_name = 'admin/jobtype.html'
    
    def post(self,request):
        jobtype = request.POST['job_type']
               
        se = job_type()
        se.jobtype = jobtype
        se.save()
        return render(request, 'admin/index.html', {'message': "added successfull"})
    
class AddTrainingSec(TemplateView):
    template_name = 'admin/addtrainingsec.html'
    
    def post(self,request):
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        video = request.FILES['video']
        fii=FileSystemStorage()
        filesss=fii.save(video.name,video)
               
        se = Training_Section()
        
        se.title = title
        se.category = category
        se.description = description
        se.video = filesss
        se.status = "added"
        se.save()
        return render(request, 'admin/index.html', {'message': "added successfull"})
    
class ViewCategory(TemplateView):
    template_name = 'admin/training_cat.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCategory,self).get_context_data(**kwargs)
        ski = Training_Section.objects.all()

        context['ski'] = ski
        return context
    
class ViewTrainingSec(TemplateView):
    template_name = 'admin/viewtrainingsec.html'
    def get_context_data(self, **kwargs):
        context = super(ViewTrainingSec,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = Training_Section.objects.filter(id=id)

        context['ski'] = ski
        return context
    
class TrainingSecDetails(TemplateView):
    template_name = 'admin/trainingsession.html'
    def get_context_data(self, **kwargs):
        context = super(TrainingSecDetails,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = Training_Section.objects.filter(id=id)

        context['ski'] = ski
        return context
    

class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        
        compl = Feedback.objects.filter(status='added')

        context['pr'] = compl
        return context