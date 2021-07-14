from django.forms import forms
from django.http import request
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def Home(request):
    leaders = LeaderShip.objects.all()
    return render(request, 'nature_club/Home.html', {'leaders':leaders})

def About(request):
    return render(request, 'nature_club/About.html')


def Contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = ContactForm()
	return render(request,'nature_club/Contact.html',{'form': form})


def events(request):
    images = Events.objects.all()
    return render(request, 'nature_club/Events.html', {'images':images})

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'nature_club/Gallery.html', {'images':images})

#SUBCOMMITTEE

def Subcom1(request):
    return render(request, 'nature_club/subcom1.html')

def Subcom2(request):
    return render(request, 'nature_club/subcom2.html')

def Subcom3(request):
    return render(request, 'nature_club/subcom3.html')



   
        
