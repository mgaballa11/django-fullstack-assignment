from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'message': 'Welcome to My Django App!',
        'today': 'April 21, 2025'
    }
    return render(request, 'home.html', context)
