from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from school.models.appSetting_model import AppSetting

from ..models.school_model import School
from ..forms.school_form import SchoolForm

# Create your views here.


def list_school(request):
    schools = School.objects.all()
    app_setting_total = AppSetting.objects.all()

    context = {
        'schools': schools,
        'app_setting_total': app_setting_total,

    }
    return render(request, 'school/list_school.html', context)


def add_school(request):
    app_setting_total = AppSetting.objects.all()
    school_total= School.objects.all()
    school_form = SchoolForm()
    context = {
        'title': 'Ajouter une Ecole',
        'school_form': school_form,
        'school_total':school_total,
        'app_setting_total':app_setting_total,
    }

    if request.method == 'POST':
        school_form = SchoolForm(request.POST)
        if school_form.is_valid():
            school_form.save()
            return redirect('school:check_school')
        else:
            school_form = SchoolForm()


    schools= School.objects.all()
    if not schools :
        return render(request, 'school/add_school.html',context)
    else :
        return redirect('login:signin') #connexion



def update_school(request):
    app_setting_total = AppSetting.objects.all()
    school_total= School.objects.all()
    context = {
        "title": 'Modifier Ecole',
        "app_setting_total": app_setting_total,
        "school_total": school_total,
    }

    try:
        school = School.objects.first()
    except ObjectDoesNotExist:
        print(f"School does not exist !!")
        return redirect('school:list_school')

    if request.method == 'POST':
        school_form = SchoolForm(data=request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return redirect('school:list_school')
    school_form = SchoolForm(instance=school)
    context["school_form"] = school_form

    return render(request, 'school/add_school.html', context)



def delete_school(request,id):
    try:
        school = School.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"School does not exist !!")
        return redirect('school:list_school')

    school.delete()
    return redirect('school:list_school')



def check_school(request):

    school = School.objects.all()

    if not school:
        return redirect('school:add_appSetting')
    else:
        return redirect('login:signin')
