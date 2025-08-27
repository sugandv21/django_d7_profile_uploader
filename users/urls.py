from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
]
