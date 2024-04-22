from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from app.models import *

class Indexview(TemplateView):
    template_name = 'skilledworkers/index.html'

class AddJobDetails(TemplateView):
    template_name = 'skilledworkers/addjobdetails.html'
    def get_context_data(self, **kwargs):
        context = super(AddJobDetails,self).get_context_data(**kwargs)

        ski = job_type.objects.all()

        context['ski'] = ski
        return context
    
    def post(self,request):
        swrk=skilled_worker.objects.get(user_id=self.request.user.id)
        jobtype = request.POST['job_type']
        experience = request.POST['experience']
        description = request.POST['description']
               
        se = skilled_worker_details()
        se.sworker_id = swrk.id
        se.jobtype = jobtype
        se.experience = experience
        se.description = description
        se.save()
        return render(request, 'skilledworkers/index.html', {'message': "added successfull"})
    

class ViewBookings(TemplateView):
    template_name = 'skilledworkers/viewbookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBookings,self).get_context_data(**kwargs)
        swrk=skilled_worker.objects.get(user_id=self.request.user.id)
        ski = Services.objects.filter(sworker__sworker_id=swrk.id)

        context['ski'] = ski
        return context

class Approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = Services.objects.get(pk=id)
        user.status='approved'
        user.save()
        return render(request,'skilledworkers/index.html',{'message':" Account Approved"})
    

class Reject(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = Services.objects.get(pk=id)
        user.status='rejected'
        user.save()
        return render(request,'skilledworkers/index.html',{'message':" Account Approved"})
    
class Completed(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = Services.objects.get(pk=id)
        user.status='completed'
        user.save()
        return render(request,'skilledworkers/index.html',{'message':" Account Approved"})
    

class view_feedback(TemplateView):
    template_name = 'skilledworkers/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        shop= Services.objects.get(sworker__sworker__user_id=self.request.user.id)
        compl = Feedback.objects.filter(status='added', service_id=shop.id)

        context['pr'] = compl
        return context