from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'role', 'age', 'email', 'is_active']


class SignupForm(UserCreationForm):

    username = forms.CharField(
        max_length=30,
        help_text="Max 30 characters. Letters and numbers only."
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']