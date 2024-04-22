from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from app.models import *

class Indexview(TemplateView):
    template_name = 'user/index.html'

class ViewWorkers(TemplateView):
    template_name = 'user/viewworkers.html'
    def get_context_data(self, **kwargs):
        context = super(ViewWorkers,self).get_context_data(**kwargs)

        ski = skilled_worker_details.objects.all()

        context['ski'] = ski
        return context
    
class BookService(TemplateView):
    template_name = 'user/bookworker.html'
    def get_context_data(self, **kwargs):
        context = super(BookService,self).get_context_data(**kwargs)
        id=self.request.GET["id"]
        ski = skilled_worker_details.objects.filter(id=id)

        context['ski'] = ski
        return context
    
    def post(self,request):
        swrk=user_reg.objects.get(user_id=self.request.user.id)
        date = request.POST['date']
        time = request.POST['time']
        description = request.POST['description']
        id = request.POST['id']
        se = Services()
        
        se.user_id = swrk.id
        se.sworker_id = id
        se.date = date
        se.time = time
        se.description = description
        se.status = "added"
        se.save()
        return render(request, 'user/index.html', {'message': "added successfull"})
    

class ViewBookings(TemplateView):
    template_name = 'user/viewbookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBookings,self).get_context_data(**kwargs)
        swrk=user_reg.objects.get(user_id=self.request.user.id)
        ski = Services.objects.filter(user_id=swrk.id)

        context['ski'] = ski
        return context
    
class Add_feedback(TemplateView):
    template_name = 'user/feedback.html'

    def post(self, request, *args, **kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)
        id=self.request.GET['id']
        product=Services.objects.get(id=id)
        subject=request.POST['subject']
        feedback=request.POST['feedback']

        feed = Feedback()
        feed.user_id=user.id
        feed.service_id=product.id
        feed.subject=subject
        feed.feedback=feedback
        feed.status = 'added'
        feed.save()
        return render(request, 'user/index.html', {'message': "feedback added"})
    

class feedback_view(TemplateView):
    template_name= 'user/feedback_view.html'
    def get_context_data(self, **kwargs):
        context = super(feedback_view, self).get_context_data(**kwargs)
        user=user_reg.objects.get(user_id=self.request.user.id)
        pr = Feedback.objects.filter(user_id=user.id)
        context['pr'] = pr

        return context