from django.db.models import fields
from .models import Business, NeighborHood, Profile
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact','location','neighborhood')

class HoodForm(forms.ModelForm):
    class Meta:
        model=NeighborHood
        fields = ['photo','name','content','occupants_count','location']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['business_name','email','description','location','neighborhood']