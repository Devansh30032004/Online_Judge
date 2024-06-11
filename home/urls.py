"""
URL configuration for online_judge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
     path('',views.home,name='home'),
     path('problems/', views.problem_list, name='problem_list'),
     path('submissions/',views.submission_list , name='submission-list'),
     path('login/',views.login_user, name='login'),
     path('register/', views.register_user, name='register'),
     path('logout/', views.logout_user, name='logout'),
     path('profile/',views.profile, name = 'profile'),
     path('problem/<int:pk>/', views.problem_detail, name='problem_detail'),
     path('problem/<int:problem_id>/submit/', views.submit_code, name='submit_code'),
     path('run/', views.run_code, name='run_code'),
     path('submission/<int:submission_id>/', views.submission_detail, name='submission_detail'),
     path('view_code/<int:submission_id>/', views.view_code, name='view_code'),
]
