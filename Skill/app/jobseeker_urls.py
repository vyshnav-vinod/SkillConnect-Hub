from django.urls import path
from app.jobseeker_views import *

urlpatterns = [
    path('',Indexview.as_view()),
    path('AddApplication',AddApplication.as_view()),
     path('ViewJobApplications',ViewJobApplications.as_view()),
     path('ViewInterview',ViewInterview.as_view()),
         path('ViewTrainingSec',ViewTrainingSec.as_view()),
    path('ViewCategory',ViewCategory.as_view()),
    path('TrainingSecDetails',TrainingSecDetails.as_view())

    ]
def urls():
    return urlpatterns, 'job_seeker', 'job_seeker'