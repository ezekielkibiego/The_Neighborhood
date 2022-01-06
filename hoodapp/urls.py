from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index ,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    # path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path("create_business", views.create_business, name="create_business"),
    path("business/", views.business, name="business"),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood'),
    path('hood/<str:name>',views.single_hood,name='single_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    
    
]