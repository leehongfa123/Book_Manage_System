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
from Author_manager import views
urlpatterns = [

    path('main/', views.author, name = 'author'),
    # path('author/', views.author, name = 'author'),
    path('all_authors/', views.all_authors, name = 'all_authors'),
    path('add_author/', views.add_author, name = 'add_author'),
    path('find_author/', views.find_author, name = 'find_author'),

    re_path('del/(\d+)/', views.del_author, name = 'del_author'),
    re_path('edit/(\d+)/', views.edit_author, name = 'edit_author'),

]
