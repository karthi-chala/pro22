"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from app1 import views
views_app1=views
from app2 import views
views_app2=views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/',views_app1.index,name='index1'),
    path('index2/',views_app2.index,name='index2'),
    path('sample1/',views_app1.sample,name='sample1'),
    path('sample2/',views_app2.sample,name='sample2'),

]
