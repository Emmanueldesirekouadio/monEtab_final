from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from school.models.school_model import School
from school.models.appSetting_model import AppSetting
from user.forms.user_form import UserAppForms

# Create your views here.
def signup(request):
    print(f"username : {request.POST.get('identifiant')}")
    if request.method == 'POST':
        username = request.POST['identifiant']
        password = request.POST['password']
        if not username or not password:
            return render (request, 'login/signup.html')
        user = UserAppForms(request.POST)
        if user.is_valid():
            user.save(commit=False)
            user.password = request.POST.cleaned_data['password']
            user.set_password(user.password) 
            user.save()
            login(request, user)
        return redirect('dashboard:dashboard')

    return render(request, 'login/signup.html')


def login_view(request): 
    app_setting = AppSetting.objects.all()
    school = School.objects.all()

    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')

    if not app_setting:
        return redirect('school:add_appSetting')
    
    if not school:
        return redirect('school:add_appSetting')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                return redirect('dashboard:dashboard')
            else :
                return redirect('login:signin')
    else:
        form = AuthenticationForm()
    return render(request, 'login/signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login:signin')



def add(request):
    context={"title":"Ajouter Utilisateur"}
    if request.method == "POST":
        print(request.POST)
        form =UserAppForms(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.password = form.cleaned_data["password"]
            user.set_password(user.password)
            user.save()
            login(request,user)
            return redirect('user:index')
        else:
            return render(request,"user/add.html")

    # context={'elev_form':elev_form}
    form = UserAppForms()
    context["form"] = form

    return render(request,"user/add.html",context)