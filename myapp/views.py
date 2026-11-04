
from myapp.models import Profile
from django.shortcuts import render, redirect
from myapp.forms import ProfileForm

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "myapp/profile_list.html", {"profiles": profiles})

def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm()
    return render(request, "myapp/profile_form.html", {"form": form, "title": "Nuevo perfil"})