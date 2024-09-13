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

from user.views import adresse_view
from .views import *

app_name = 'user'

urlpatterns = [
     
    # User CRUD Operations
    path('', user_view.list_user, name='list_user'),
    path('add_user', user_view.add_user, name='add_user'),
    path('update_user/<int:id>', user_view.update_user, name='update_user'),
    path('delete_user/<int:id>', user_view.delete_user, name='delete_user'),

    # Adresse CRUD Operations
    path('list_adresse', adresse_view.list_adresse, name='list_adresse'),
    path('add_adresse', adresse_view.add_adresse, name='add_adresse'),
    path('update_adresse/<int:id>', adresse_view.update_adresse, name='update_adresse'),
    path('delete_adresse/<int:id>', adresse_view.delete_adresse, name='delete_adresse'),

    # RoleUser CRUD Operations
    path('list_roleUser', roleUser_view.list_roleUser, name='list_roleUser'),
    path('add_roleUser', roleUser_view.add_roleUser, name='add_roleUser'),
    path('update_roleUser/<int:id>', roleUser_view.update_roleUser, name='update_roleUser'),
    path('delete_roleUser/<int:id>', roleUser_view.delete_roleUser, name='delete_roleUser'),

    path('deactivate_user/<int:id>', user_view.deactivate_user, name='deactivate_user'),







]


