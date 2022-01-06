from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from hoodapp.forms import BusinessForm, HoodForm, ProfileForm, UpdateProfileForm
from hoodapp.models import Profile



@login_required(login_url="/accounts/login/")
def index(request):
    hood = NeighborHood.objects.all().order_by('-id')
    return render(request, 'index.html',{'hood': hood})

# @login_required(login_url='/accounts/login/')
# def create_profile(request):
#     current_user = request.user
#     title = "Create Profile"
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return HttpResponseRedirect('/')

#     else:
#         form = ProfileForm()
#     return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    neighborhood = NeighborHood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    return render(request, "profile.html", {"profile": profile, ' neighborhood':  neighborhood, 'businesses': businesses})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})


@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        b_form=BusinessForm(request.POST,request.FILES)

        if b_form.is_valid():
            business=b_form.save(commit=False)
            business.user=current_user
            business.save()
        return HttpResponseRedirect('/business')
    else:
        b_form=BusinessForm()
    return render (request,'create_business.html', {'b_form': b_form, 'profile': profile})




@login_required(login_url="/accounts/login/")
def business(request):
    current_user = request.user
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighborhood = NeighborHood.objects.all()
        
        businesses = Business.objects.filter(user_id=current_user.id)
        
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.filter(
            neighborhood=profile.neighborhood)
        return render(request, "business.html", {"businesses": businesses})

@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/hood')
    else:
        hood_form = HoodForm()
    context = {'hood_form':hood_form}
    return render(request, 'hood_form.html',context)

@login_required(login_url="/accounts/login/")
def hood(request):
    current_user = request.user
    hood = NeighborHood.objects.all().order_by('-id')
    return render(request, 'hoods.html', {'hood': hood})

@login_required(login_url='/accounts/login/')
def single_hood(request,name):
    current_user = request.user
    hood = NeighborHood.objects.get(name=name)
    businesses = Business.objects.filter(user_id=current_user.id)
    return render(request,'single_hood.html',{'hood':hood,'businesses': businesses})

def join_hood(request,id):
    neighborhood = get_object_or_404(NeighborHood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')    