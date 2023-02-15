"""GMAO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import tasks.views as views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-machines', views.add_machine, name="add-machine"),
    path('add-pannes', views.add_panne, name="add-panne"),
    path('admin/', admin.site.urls),
    path('machines/', views.machine_list, name='machines'),
    path('pannes/', views.panne_list, name='pannes'),
    path('pannes/update-panne/<int:pk>/', views.update_panne, name='update-panne'),
    path('pannes/delete-panne/<int:pk>/', views.delete_panne, name='delete-panne'),
]