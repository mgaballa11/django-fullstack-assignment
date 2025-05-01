from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

def home(request):
    context = {
        'message': 'Welcome to My Django App!',
        'today': 'April 21, 2025'
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})