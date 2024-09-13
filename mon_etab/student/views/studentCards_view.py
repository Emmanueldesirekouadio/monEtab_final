from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from ..models.studentCards_model import StudentCards
from ..forms.studentCards_form import StudentCardsForms
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting

# Create your views here.

@login_required()
def list_studentCards(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    studentCards = StudentCards.objects.all()
    context = {
        'studentCards': studentCards,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'studentCards/list_studentCards.html', context)


@login_required()
def add_studentCards(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    studentCards_form = StudentCardsForms()

    if request.method == 'POST':
        studentCards_form = StudentCardsForms(request.POST)
        if studentCards_form.is_valid():
            studentCards_form.save()
            return redirect('student:list_studentCards')

    context = {
        'title': 'Ajouter une Carte Eleve',
        'studentCards_form': studentCards_form,
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, 'studentCards/add_studentCards.html',context)

@login_required()
def update_studentCards(request, id):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        "title": 'Modifier une Carte Eleve',
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    try:
        studentCard = StudentCards.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Student Cards does not exist !!")
        return redirect('student:list_studentCards')

    if request.method == 'POST':
        studentCards_form = StudentCardsForms(data=request.POST, instance=studentCard)
        if studentCards_form.is_valid():
            studentCards_form.save()
            return redirect('student:list_studentCards')
    studentCards_form = StudentCardsForms(instance=studentCard)
    context["studentCards_form"] = studentCards_form

    return render(request, 'studentCards/add_studentCards.html', context)


@login_required()
def delete_studentCards(request,id):
    try:
        studentCards = StudentCards.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"studentCards does not exist !!")
        return redirect('student:list_studentCards')

    studentCards.delete()
    return redirect('student:list_studentCards')
