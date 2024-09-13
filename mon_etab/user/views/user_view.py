from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from teacher.models.teacher_model import Teacher

from ..models.user_model import UserApps
from ..forms.user_form import UserAppForms
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting

# Create your views here.


@login_required()
def list_user(request):
    search_area = request.GET.get('name')
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    if search_area:
        search_user = UserApps.objects.filter(username__icontains = search_area )
        # print(f"user status :  {search_user.values_list}")
        count_user = search_user.count()
        context = {
            'users':search_user,
            'count_user': count_user,
            'app_setting_total': app_setting_total,
            'school_total': school_total,
        }
    else :
        users = UserApps.objects.all()

        count_user = users.count()
        context = {
            'users': users,
            'count_user': count_user,
            'app_setting_total': app_setting_total,
            'school_total': school_total,
        }
    return render(request, 'user/list_user.html', context)


@login_required()
def add_user(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()
    user_form = UserAppForms()

    if request.method == 'POST':

        print(f"request.POST.get('password') : {request.POST.get('password')}")
        user_form = UserAppForms(request.POST)
        if user_form.is_valid():
            print(f'user password : {user_form.save().password}' )
            user_form.save(commit=False).set_password(user_form.save().password)
            user_form.save()
            # user_form.save().set_password(user_form.save().password)

            return redirect('user:list_user')

    context = {
        'title': 'Ajouter un Utilisateur',
        'user_form': user_form,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'user/add_user.html',context)


@login_required()
def update_user(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        "title": 'Modifier Utilisateur',
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    try:
        user = UserApps.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"User does not exist !!")
        return redirect('user:list_user')

    if request.method == 'POST':
        user_form = UserAppForms(data=request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list_user')
    user_form = UserAppForms(instance=user)
    context["user_form"] = user_form

    return render(request, 'user/add_user.html', context)


@login_required()
def delete_user(request, id):
    try:
        user = UserApps.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"user does not exist !!")
        return redirect('user:list_user')

    user.delete()
    return redirect('user:list_user')



def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # if not username in request.Post

    if not username and not password:
        return redirect('user:login')

    check_username = UserApps.objects.filter(username__exact = username, password__exact = password)
    if not check_username:
        print("Wrong connexion !!!!")
        return redirect('user:login')
    return redirect('school:check_app_setting')


@login_required()
def deactivate_user(request,id):
    try:
        user = UserApps.objects.get(id=id)
        print(f"status user : {user.is_active}")

    except ObjectDoesNotExist:
        return redirect('user:list_user')

    user.is_active = False
    print(f"status user after search : {user.is_active}")

    user.save()
    context = {
        'users' : UserApps.objects.all(),
        'count_user': UserApps.objects.all().count(),
    }

    return render(request, 'user/list_user.html', context)

