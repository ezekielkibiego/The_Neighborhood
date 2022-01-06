from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.dispatch import receiver
from django.db.models.signals import post_save



class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField("image",null=True)
    content = models.TextField(max_length=600, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    contact = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def _str_(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def __str__(self):
        return self.business_name

