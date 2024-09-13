from django.urls import path, include
from rest_framework import routers
from .api_views.student_api_view import student_list,student_detail
from .api_views.teacher_api_view import teacher_list
from .api_views.user_api_view import user_list
from .api_views.absence_api_view import absence_list
from .api_views.app_setting_api_view import app_setting_list
from .api_views.role_user_api_view import role_user_list
from .api_views.school_api_view import school_list
from .api_views.student_card_api_view import student_card_list

router = routers.DefaultRouter()
#router.register(prefix

urlpatterns = [

    path('students/',student_list),
    path('students/<int:pk>/',student_detail),




    path('teachers/',teacher_list),
    path('users/',user_list),
    path('absence/',absence_list),
    path('app_settings/',app_setting_list),
    path('role_users/',role_user_list),
    path('schools/',school_list),
    path('student_cards/',student_card_list),

]