from django.urls import path
from app.privatesector_views import *

urlpatterns = [
    path('',Indexview.as_view()),
    path('AddVacancy',AddVacancy.as_view()),
    path('ViewVacancy',ViewVacancy.as_view()),
    path('ViewJobApplications',ViewJobApplications.as_view()),
    path('Approve',Approve.as_view()),
    path('Reject',Reject.as_view()),
    path('ScheduleInterview',ScheduleInterview.as_view()),
    path('ViewInterview',ViewInterview.as_view()),
    path("DeleteVacancy/<pk>", VacancyDeleteView.as_view()),

    ]
def urls():
    return urlpatterns, 'priv_sect', 'priv_sect'