from django.contrib import admin
from .models import Business, Profile,NeighborHood,Location


admin.site.register(Profile)
admin.site.register(NeighborHood)
admin.site.register(Location)
admin.site.register(Business)