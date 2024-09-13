from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from student.models.student_model import Student
from teacher.models.teacher_model import Teacher
from user.models.user_model import UserApps
from django.contrib.auth.decorators import login_required
from school.models.school_model import School
from school.models.appSetting_model import AppSetting
#from docx import Document
# Create your views here.


@login_required()
def rapport(request):
    app_setting_total = AppSetting.objects.all()
    school_total = School.objects.all()

    context = {
        'app_setting_total': app_setting_total,
        'school_total': school_total,
    }
    return render(request, "rapport/rapport.html", context)


@login_required()
@csrf_exempt
def export_data(request):
    if request.method == 'POST':
        export_type = request.POST.get('classe')  # Choix entre élève, professeur ou utilisateur
        file_type = request.POST.get('export_type')  # Choix entre Excel ou PDF

        # Choisir le modèle en fonction du type d'exportation
        if export_type == 'Listes_des_eleves':
            model = Student
        elif export_type == 'Listes_des_professeurs':
            model = Teacher
        elif export_type == 'Listes_des_utilisateur':
            model = UserApps
        else:
            return HttpResponse("Type d'exportation invalide.", status=400)

        # Extraire les données du modèle choisi
        data = model.objects.all().values()

        if file_type == 'excel':
            # Exporter les données en Excel
            df = pd.DataFrame(list(data))

            # Convertir les colonnes datetime pour qu'elles soient "timezone-naive"
            for column in df.select_dtypes(include=['datetime64[ns, UTC]', 'datetime64[ns]']):
                df[column] = df[column].dt.tz_localize(None)

            # Créer la réponse pour le fichier Excel
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={export_type}_exporté.xlsx'

            # Utiliser pandas pour écrire les données dans un fichier Excel
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Données')

            return response

        elif file_type == 'pdf':
            # Créer un fichier PDF
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter

            # Ajouter un titre
            p.drawString(100, height - 100, f'Données {export_type.capitalize()} Exportées')

            # Ajouter les données dans le PDF
            y = height - 140
            for item in data:
                for field, value in item.items():
                    if isinstance(value, datetime):
                        # Si c'est un objet datetime avec fuseau horaire, on retire le fuseau horaire
                        if value.tzinfo is not None:
                            value = value.replace(tzinfo=None)
                        # Formater la date comme chaîne
                        value = value.strftime('%Y-%m-%d %H:%M:%S')

                    # Écrire les données dans le PDF
                    p.drawString(100, y, f'{field}: {value}')
                    y -= 20

            p.showPage()
            p.save()

            buffer.seek(0)
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={export_type}_exporté.pdf'

            return response

    return HttpResponse(status=405)  # Méthode non autorisée si autre chose que POST