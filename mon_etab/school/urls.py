from django.urls import path
from school.views import school_view
from school.views import appSetting_view


app_name = 'school'

urlpatterns = [
    path('school/list_school', school_view.list_school, name='list_school'),
    path('school/add_school', school_view.add_school, name='add_school'),
    path('update_school', school_view.update_school, name='update_school'),
    path('school/delete_school/<int:id>', school_view.delete_school, name='delete_school'),

    path('school/', school_view.check_school, name='check_school'),





    path('', appSetting_view.check_app_setting, name='check_app_setting'),



    path('list_appSetting', appSetting_view.list_appSetting, name='list_appSetting'),
    path('add_appSetting', appSetting_view.add_appSetting, name='add_appSetting'),
    path('update_appSetting', appSetting_view.update_appSetting, name='update_appSetting'),
    path('delete_appSetting/<int:id>', appSetting_view.delete_appSetting, name='delete_appSetting'),

]
