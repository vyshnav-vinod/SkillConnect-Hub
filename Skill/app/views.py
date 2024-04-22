from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from app.models import *


class Indexview(TemplateView):
    template_name = 'index.html'
    
class CustomerReg(TemplateView):
    template_name = 'registration.html'

    def post(self,request):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['user_name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['your_email']
        password = request.POST['password']
        password2 = request.POST['comfirm_password']
        
        if password == password2:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'registration.html',{'message':"already added the username or email"})
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name='1')
                user.save()
                se = user_reg()
                se.user = user
                se.phone = phone
                se.address=address
                se.lname=lname
                se.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "user"
                usertype.save()
                return render(request, 'index.html', {'message': "Registration successfull"})
        else:
            return render(request, 'registration.html', {'message': "Passwords does not match"})

class loginview(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['user_name']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "job_seeker":
                    return redirect('/jobseeker')
                elif UserType.objects.get(user_id=user.id).type == "priv_sect":
                    return redirect('/privatesectors')
                else:
                    return redirect('/skilled_workers')
            else:
                return render(request,'login.html',{'message':" User Account Not Approved"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})

class jobreisterview(TemplateView):
    template_name = 'jobregistration.html'

    def post(self,request):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['user_name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['your_email']
        password = request.POST['password']
        password2 = request.POST['comfirm_password']
        
        if password == password2:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'jobregistration.html',{'message':"already added the username or email"})
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name='0')
                user.save()
                se = job_seeker()
                se.user = user
                se.phone = phone
                se.address=address
                se.lname=lname
                se.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "job_seeker"
                usertype.save()
                return render(request, 'index.html', {'message': "Registration successfull"})
        else:
            return render(request, 'jobregistration.html', {'message': "Passwords does not match"})
        

class privsectregview(TemplateView):
    template_name = 'privatesectorregis.html'

    def post(self,request):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['user_name']
        phone=request.POST['phone']
        licence_file=request.FILES['licence']
        fii=FileSystemStorage()
        filesss=fii.save(licence_file.name,licence_file)
        address=request.POST['address']
        email= request.POST['your_email']
        password = request.POST['password']
        password2 = request.POST['comfirm_password']
        
        if password == password2:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'privatesectorregis.html',{'message':"already added the username or email"})
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name='0')
                user.save()
                se = priv_sect()
                se.user = user
                se.phone = phone
                se.address=address
                se.lname=lname
                se.licence=filesss
                se.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "priv_sect"
                usertype.save()
                return render(request, 'index.html', {'message': "Registration successfull"})
        else:
            return render(request, 'privatesectorregis.html', {'message': "Passwords does not match"})

class skilledworkerregview(TemplateView):
    template_name = 'skilledworkerregis.html'

    def post(self,request):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['user_name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['your_email']
        password = request.POST['password']
        password2 = request.POST['comfirm_password']
        
        if password == password2:
            if User.objects.filter(email=email,username=username):
                print ('pass')
                return render(request,'skilledworkerregis.html',{'message':"already added the username or email"})
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name='0')
                user.save()
                se = skilled_worker()
                se.user = user
                se.phone = phone
                se.address=address
                se.lname=lname
                se.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "skilled_worker"
                usertype.save()
                return render(request, 'index.html', {'message': "Registration successfull"})
        else:
            return render(request, 'skilledworkerregis.html', {'message': "Passwords does not match"})


