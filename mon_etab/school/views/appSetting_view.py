from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from school.models.school_model import School

from ..models.appSetting_model import AppSetting
from ..forms.appSetting_form import AppSettingForm

# Create your views here.

def list_appSetting(request):
    appSettings = AppSetting.objects.all()
    school_total = School.objects.all()
    appSetting_form = AppSettingForm()

    context = {
        'appSettings': appSettings,
        'school_total': school_total,

    }
    return render(request, 'appSetting/list_appSetting.html', context)

def add_appSetting(request):

    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    if request.method == 'POST':
     formsetting = AppSettingForm(request.POST)
     if formsetting.is_valid():
        formsetting.save()
        return redirect('school:add_school')
    else:
       formsetting = AppSettingForm()

    app_setting= AppSetting.objects.all()
    if not app_setting:
        return render(request, 'appSetting/add_appSetting.html', {'appSetting_form':formsetting, 'app_setting_total':app_setting_total})

    else :
       return redirect('school:add_school')#ajouter ecole




def update_appSetting(request):
    app_setting_total = AppSetting.objects.all()
    shool_total = School.objects.all()
    context = {
        "title": 'Modifier un Reglage Application',
        "app_setting_total": app_setting_total,
        "school_total": shool_total,
    }
    try:
        appSetting = AppSetting.objects.first()
    except ObjectDoesNotExist:
        print(f"AppSettings does not exist !!")
        return redirect('school:list_appSetting')

    if request.method == 'POST':
        appSetting_form = AppSettingForm(data=request.POST, instance=appSetting)
        if appSetting_form.is_valid():
            appSetting_form.save()
            return redirect('school:list_appSetting')
    appSetting_form = AppSettingForm(instance=appSetting)
    context["appSetting_form"] = appSetting_form
    return render(request, 'appSetting/add_appSetting.html', context)


def delete_appSetting(request,id):
    try:
        appSetting = AppSetting.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"AppSettings does not exist !!")
        return redirect('school:list_appSetting')

    appSetting.delete()
    return redirect('school:list_appSetting')


def check_app_setting(request):

    app_setting = AppSetting.objects.all()
    if not app_setting:
        return redirect('school:add_appSetting')
    else:
        return redirect('school:add_appSetting')
