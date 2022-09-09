from django.shortcuts import render
from django.http import HttpResponse

# Creates the base html file for every page 
def index(request):
    return render(request, 'base.html')

# this is the home page of the webise 
def home(request):
    return render(request, 'home.html')

 