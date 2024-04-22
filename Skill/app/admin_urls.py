from django.urls import path
from app.admin_views import *

urlpatterns = [
    path('',Indexview.as_view()),
    path('jobtype',jobtype.as_view()),
    path('user_verify',user_verify.as_view()),
    path('approve',user_approve.as_view()),
    path('reject',user_reject.as_view()),
    path('jobseekerview',jobseeker_view.as_view()),
    path('privsect_verify',privsect_verify.as_view()),
    path('approve',privsect_approve.as_view()),
    path('reject',privsect_reject.as_view()),
    path('privsectview',privsect_view.as_view()),
    path('skillwrkr_verify',skillwrkr_verify.as_view()),
    path('approve',skillwrkr_approve.as_view()),
    path('reject',skillwrkr_reject.as_view()),
    path('skillwrkrview',skillwrkr_view.as_view()),
    path('ViewBookings',ViewBookings.as_view()),
    path('ViewJobApplications',ViewJobApplications.as_view()),
    path('ViewInterview',ViewInterview.as_view()),
    path('ViewVacancy',ViewVacancy.as_view()),
    path('AddTrainingSec',AddTrainingSec.as_view()),
    path('ViewTrainingSec',ViewTrainingSec.as_view()),
    path('ViewCategory',ViewCategory.as_view()),
    path('TrainingSecDetails',TrainingSecDetails.as_view()),
    path('view_feedback',view_feedback.as_view())
    ]

def urls():
    return urlpatterns, 'admin', 'admin'