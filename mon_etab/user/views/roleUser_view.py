from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from ..models.roleUser_model import RoleUser
from ..forms.roleUser_form import RoleUserForms
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting

# Create your views here.


@login_required()
def list_roleUser(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    roleUsers = RoleUser.objects.all()
    context = {
        'roleUsers': roleUsers,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'roleUser/list_roleUser.html', context)


@login_required()
def add_roleUser(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    roleUsers_form = RoleUserForms()

    if request.method == 'POST':
        roleUsers_form = RoleUserForms(request.POST)
        if roleUsers_form.is_valid():
            roleUsers_form.save()
            return redirect('user:list_roleUser')

    context = {
        'title': 'Ajouter un Role Utilisateur',
        'roleUsers_form': roleUsers_form,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'roleUser/add_roleUser.html',context)


@login_required()
def update_roleUser(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    context = {
        "title": 'Modifier Role Utilisateur',
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    try:
        roleUser = RoleUser.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"RoleUser does not exist !!")
        return redirect('user:list_roleUser')

    if request.method == 'POST':
        roleUsers_form = RoleUserForms(data=request.POST, instance=roleUser)
        if roleUsers_form.is_valid():
            roleUsers_form.save()
            return redirect('user:list_roleUser')
    roleUsers_form = RoleUserForms(instance=roleUser)
    context["roleUsers_form"] = roleUsers_form

    return render(request, 'roleUser/add_roleUser.html', context)


@login_required()
def delete_roleUser(request,id):
    try:
        roleUser = RoleUser.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"RoleUser does not exist !!")
        return redirect('user:list_roleUser')

    roleUser.delete()
    return redirect('user:list_roleUser')
