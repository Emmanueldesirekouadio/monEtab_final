from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models.teacher_model import Teacher
from .forms.teacher_form import TeacherForms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting


# Create your views here.

@login_required()
def list_teacher(request):
    app_setting_total = AppSetting.objects.all()
    school_total= School.objects.all()

    search_area = request.GET.get('name')

    if search_area:
        search_teacher = Teacher.objects.filter(user__pseudo__icontains = search_area )
        count_teacher = search_teacher.count()
        context = {
            'teachers':search_teacher,
            'count_teacher': count_teacher,
            'app_setting_total': app_setting_total,
            'school_total': school_total,
        }
    else :
        teachers = Teacher.objects.all()
        count_teacher = teachers.count()
        context = {
            'teachers': teachers,
            'title': 'Liste des Professeurs',
            'count_teacher': count_teacher,
            'app_setting_total': app_setting_total,
            'school_total': school_total,
        }
    return render(request, 'teacher/list_teacher.html',context)




@login_required()
def add_teacher(request):
    app_setting_total = AppSetting.objects.all()
    school_total= School.objects.all()

    teacher = TeacherForms()

    if request.method == 'POST':
        teacher = TeacherForms(data=request.POST)
        if teacher.is_valid():
            print(f"teacher : {teacher}")
            teacher.save()
            return redirect('teacher:list_teacher')
            # return redirect('teacher/list_teacher.html')
            # return return(request, 'teacher/list_teacher.html')

    context = {
        'title': 'Ajouter un Professeur',
        'teacher': teacher,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }

    return render(request, 'teacher/add_teacher.html', context)


@login_required()
def update_teacher(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        "title": 'Modifier Professeur',
        "app_setting_total": app_setting_total,
        "school_total": school_total,
    }
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist :
        print(f"Teacher does not exist !!")
        return redirect('teacher:list_teacher')

    if request.method == 'POST':
        teacher_form = TeacherForms(data=request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher.save()
            return redirect('teacher:list_teacher')

    teacher_form = TeacherForms(instance=teacher)
    context['teacher'] = teacher_form

    return render(request, 'teacher/add_teacher.html', context)


@login_required()
def delete_teacher(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist :
        print(f"Teacher does not exist !!")
        return redirect('teacher:list_teacher')

    teacher.delete()
    return redirect('teacher:list_teacher')
