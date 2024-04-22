from django.urls import path
from app.user_views import *

urlpatterns = [
    path('',Indexview.as_view()),
    path('ViewWorkers',ViewWorkers.as_view()),
    path('BookService',BookService.as_view()),
    path('ViewBookings',ViewBookings.as_view()),
    path('Add_feedback',Add_feedback.as_view()),
    path('feedback_view',feedback_view.as_view()),
    ]
def urls():
    return urlpatterns, 'user', 'user'