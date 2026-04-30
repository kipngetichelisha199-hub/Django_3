from django.shortcuts import render

# Create your views here.
def landing(request):
    context = {'welcomeMessage': 'Welcome to the landing page!! '} # dict that will hold out data
    return render(request, 'hobbiesApp/landing.html', context)

def home(request):
    context = {'welcomeMessage': 'Welcome to the home page!! '} # dict that will hold out data
    return render(request, 'hobbiesApp/home.html', context)

def about(request):
    context = {'welcomeMessage': 'Welcome to the about page!! '} # dict that will hold out data
    return render(request, 'hobbiesApp/about.html', context)

def contact(request):
    context = {'welcomeMessage': 'Welcome to the contacts page!! '} # dict that will hold out data
    return render(request, 'hobbiesApp/contact.html', context)

def projects(request):
    context = {'welcomeMessage': 'Welcome to the projects page!! '} # dict that will hold out data
    return render(request, 'hobbiesApp/projects.html', context)
 

# Create your views here.
