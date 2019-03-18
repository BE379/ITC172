from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resources.html/', views.resources, name='resources'),
    path('meetings/', views.getmeetings, name='getmeetings'),
    path('meetingminutes/<int:id>', views.meetingminutes, name='minutes'),
    path('newResource/', views.newResource, name='newresource'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]