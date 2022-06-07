from html.entities import html5
from pydoc import html
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    context = {
        "name":"Mojuby",
        "school":"unilorin",
        "status":"dating",
        "form":UserCreationForm()
    }
    return render(request, 'django-home/home.html', context)

def about(request):
    return render(request, 'home/about.html') 


