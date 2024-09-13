from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting
# Create your views here.


@login_required()
def homeDashboard(request):

    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        'app_setting_total': app_setting_total,
        'school_total': school_total
    }


    return render(request, 'dashboard/index.html', context)
