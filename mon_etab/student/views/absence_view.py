from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from ..models.absence_model import Absence
from ..forms.absence_form import AbsenceForms

from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting

# Create your views here.

@login_required()
def list_absence(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    absences = Absence.objects.all()
    context = {
        'absences': absences,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'absence/list_absence.html', context)

@login_required()
def add_absence(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    absence_form = AbsenceForms()

    if request.method == 'POST':
        absence_form = AbsenceForms(request.POST)
        if absence_form.is_valid():
            absence_form.save()
            return redirect('student:list_student')

    context = {
        'title': 'Ajouter une Absence',
        'absence_form': absence_form,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'absence/add_absence.html',context)


@login_required()
def update_absence(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        "title": 'Modifier une Absence',
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    try:
        absence = Absence.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Absence does not exist !!")
        return redirect('student:list_absence')

    if request.method == 'POST':
        absence_form = AbsenceForms(data=request.POST, instance=absence)
        if absence_form.is_valid():
            absence_form.save()
            return redirect('student:list_absence')
    absence_form = AbsenceForms(instance=absence)
    context["absence_form"] = absence_form

    return render(request, 'absence/add_absence.html', context)


@login_required()
def delete_absence(request,id):
    try:
        absence = Absence.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Absence does not exist !!")
        return redirect('student:list_absence')

    absence.delete()
    return redirect('student:list_absence')
