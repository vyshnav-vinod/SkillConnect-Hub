from django.urls import path
from app.skilledworker_views import *

urlpatterns = [
    path('',Indexview.as_view()),
    path('AddJobDetails',AddJobDetails.as_view()),
    path('ViewBookings',ViewBookings.as_view()),
    path('Approve',Approve.as_view()),
    path('Reject',Reject.as_view()),
    path('Completed',Completed.as_view()),
    path('view_feedback',view_feedback.as_view()),
    ]
def urls():
    return urlpatterns, 'skilled_worker', 'skilled_worker'