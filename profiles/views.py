from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required                    #Protect Pages
from .forms import SignupForm
from django.contrib.auth import login

@login_required
def home(request):
    query = request.GET.get('search', '').strip()

    profiles = Profile.objects.all().order_by('-created_at')

    if query:
        profiles = profiles.filter(
            Q(name__icontains=query) |
            Q(role__icontains=query)
        )

    paginator = Paginator(profiles, 2)  # 2 per page (testing)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "profiles": page_obj,   # ✅ IMPORTANT FIX
        "query": query
    }

    return render(request, 'profiles/home.html', context)

@login_required
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

@login_required
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

@login_required
def delete_profile(request, id):
    profile = get_object_or_404(Profile, id=id)

    if request.method == "POST":
        profile.delete()
        messages.success(request, "Profile deleted successfully 🗑")
        return redirect('home')

    return render(request, 'profiles/confirm_delete.html', {'profile': profile})


################### Signup page view ######################
def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup

            messages.success(request, "Account created successfully 🎉")
            return redirect('home')

    else:
        form = SignupForm()

    return render(request, 'profiles/signup.html', {'form': form})