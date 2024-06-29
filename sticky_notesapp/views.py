# This is the sticky_notesapp views.py

from django.shortcuts import render
from .models import User

# Create your views here.

def user_list(request):
    records = User.objects.all()
    form_records = {'records': records}
    return render(request, 'sticky_notesapp\noteslistings.html', context=form_records)


def view_home(request):
    return render(request, 'home.html')

def welcome(request):
    name = request.GET['name']
    email = request.GET['email']
    birthday = request.GET['birthday']
    context_data = {
        'name': name,
        'email': email,
        'birthday': birthday
    }
    return render(request, 'welcome.html', context=context_data)

def notes(request):
    notes = ["house", "work", "sports", "holiday", "groceries"]
    return render(request, 'notes.html', context= {'notes':notes})