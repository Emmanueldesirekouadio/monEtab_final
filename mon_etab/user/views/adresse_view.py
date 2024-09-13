from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from base.models.helpers.adresse_model import Adresse
from ..forms.adresse_form import AdresseForms
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting

# Create your views here.

@login_required()
def list_adresse(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    adresses = Adresse.objects.all()
    context = {
        'adresses': adresses,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'adresse/list_adresse.html', context)


@login_required()
def add_adresse(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all
    adresse_form = AdresseForms()

    if request.method == 'POST':
        adresse_form = AdresseForms(request.POST)
        if adresse_form.is_valid():
            adresse_form.save()
            return redirect('user:list_adresse')

    context = {
        'title': 'Ajouter une Adresse',
        'adresse_form': adresse_form,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'adresse/add_adresse.html',context)

@login_required()
def update_adresse(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        "title": 'Modifier Adresse',
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    try:
        adresse = Adresse.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Adresse does not exist !!")
        return redirect('user:list_adresse')

    if request.method == 'POST':
        adresse_form = AdresseForms(data=request.POST, instance=adresse)
        if adresse_form.is_valid():
            adresse_form.save()
            return redirect('user:list_adresse')
    adresse_form = AdresseForms(instance=adresse)
    context["adresse_form"] = adresse_form

    return render(request, 'adresse/add_adresse.html', context)


@login_required()
def delete_adresse(request,id):
    try:
        adresse = Adresse.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Adresse does not exist !!")
        return redirect('user:list_adresse')

    adresse.delete()
    return redirect('user:list_adresse')
