"""
URL configuration for ITIan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from course.views import CourseViewSet
from trainee.views import TraineeListCreateAPI, TraineeUpdateDeleteAPI

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('trainee/',include('trainee.urls')),
    path('course/',include('course.urls')),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('api/', include(router.urls)),
    path('api/trainees/', TraineeListCreateAPI.as_view(), name='trainee-list-create'),
    path('api/trainees/<int:pk>/', TraineeUpdateDeleteAPI.as_view(), name='trainee-update-delete'),
]