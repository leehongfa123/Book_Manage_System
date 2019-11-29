"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path

from Publish_manager import views
urlpatterns = [

    path('main/', views.publish_home, name = 'publish_home'),




    path('all_publishs/', views.all_publishs, name = 'all_publishs'),
    path('add_publish/', views.add_publish, name = 'add_publish'),
    path('find_publish/', views.find_publish, name = 'find_publish'),

    re_path('del/(\d+)/', views.del_publish, name = 'del_publish'),
    re_path('edit/(\d+)/', views.edit_publish, name = 'edit_publish'),

]
