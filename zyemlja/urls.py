"""
URL configuration for zyemlja project.

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
from django.urls import path
from project_app import views

from project_app.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.loginView, name = 'loginView'),
    path('dashboard/', views.dashboardView, name = 'dashboardView'),
    path('manageusers/', views.userManagementView, name = 'userManagementView'),
    path('managecourses/', views.courseManagementView, name = 'courseManagementView'),
    path('instructorCourses/', views.instructorCoursesView, name = 'instructorCoursesView'),
    path('assignmentsTA/', views.assignmentsTAView, name = 'assignmentsTAView'),
    path('contactinfo/', views.contactInfoView, name = 'contactInfoView'),
]
