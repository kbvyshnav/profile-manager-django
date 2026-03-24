from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect
from django.contrib import messages

def home(request):
    profiles = Profile.objects.filter(is_active=True)

    context = {
        "profiles": profiles
    }
    return render(request, 'profiles/home.html', context)

def add_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile added successfully ✅")
            return redirect('home')

    else:
        form = ProfileForm()

    return render(request, 'profiles/add_profile.html', {'form': form})
