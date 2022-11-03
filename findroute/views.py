from django.shortcuts import render

def home(request):
    name = 'BOB'
    return render(request, 'city_home.html', {'name': name})

def about(request):
    about = 'About as'
    return render(request, 'about.html', {'about': about})