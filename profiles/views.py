from django.shortcuts import render

def home(request):
    return render(request, 'profiles/home.html')

def add_profile(request):
    return render(request, 'profiles/add_profile.html')
