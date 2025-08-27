from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'users/home.html')

def upload_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'users/profile_upload.html', {'form': form})

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})
