from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from hoodapp.forms import ProfileForm



@login_required(login_url="/accounts/login/")
def index(request):
    
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

