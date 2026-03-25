from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

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

def update_profile(request, id):
    profile = get_object_or_404(Profile, id=id) # safely fetches object, avoids crash if not found

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile) # loads existing data, updates record instead of creating new

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully ✏️")
            return redirect('home')

    else:
        form = ProfileForm(instance=profile) # loads existing data into form(pre-filled)

    return render(request, 'profiles/add_profile.html', {'form': form})