"""
URL configuration for mon_etab project.

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
from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.list_teacher, name='list_teacher'),
    path('add_teacher', views.add_teacher, name='add_teacher'),
    path('update_teacher/<int:id>', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:id>', views.delete_teacher, name='delete_teacher'),
]
