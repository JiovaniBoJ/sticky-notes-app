# This is the sticky_notesapp urls.py

from django.urls import path, include
from .views import view_home, welcome, notes
from sticky_notesapp import views

urlpatterns = [
    path('', view_home, name='home'), 
    path('welcome/', welcome, name= 'welcome'),
    path('notes/', notes, name='notes'),
    path("", views.user_list, name='list')
    ]
  