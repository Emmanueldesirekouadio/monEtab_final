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
from .views import *

app_name = 'student'

urlpatterns = [

    # Student CRUD Operations
    path('list_student', student_view.list_student, name='list_student'),
    path('add_student', student_view.add_student, name='add_student'),
    path('update_student/<int:id>', student_view.update_student, name='update_student'),
    path('delete_student/<int:id>', student_view.delete_student, name='delete_student'),
 
    # Absence CRUD Operations
    path('list_absence', absence_view.list_absence, name='list_absence'),
    path('add_absence', absence_view.add_absence, name='add_absence'),
    path('update_absence/<int:id>', absence_view.update_absence, name='update_absence'),
    path('delete_absence/<int:id>', absence_view.delete_absence, name='delete_absence'),

     # StudendCards CRUD Operations
    path('list_studentCards', studentCards_view.list_studentCards, name='list_studentCards'),
    path('add_studentCards', studentCards_view.add_studentCards, name='add_studentCards'),
    path('update_studentCards/<int:id>', studentCards_view.update_studentCards, name='update_studentCards'),
    path('delete_studentCards/<int:id>', studentCards_view.delete_studentCards, name='delete_studentCards'),

]
