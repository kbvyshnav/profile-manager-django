from django.shortcuts import render
from .models import Profile

def home(request):
    profiles = Profile.objects.filter(is_active=True)

    context = {
        "profiles": profiles
    }
    return render(request, 'profiles/home.html', context)

def add_profile(request):
    return render(request, 'profiles/add_profile.html')
