from django.shortcuts import render,redirect
from myapp.forms import UserForm, StudentForm
import subprocess
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from myapp.models import Activity
import os

def generate_pdf(doc_path, path):
    subprocess.call(['soffice',
                 # '--headless',
                 '--convert-to',
                 'pdf',
                 '--outdir',
                 path,
                 doc_path])
    return doc_path
# soffice --convert-to pdf --outdir ./ ./sample.docx

def generate_docx(doc,context):
    doc.render(context)
    doc.save(f'static/{context['number']}.docx')
    
@login_required(login_url="/student_login")
def print_data(request,activity_id):
    if request.user.is_authenticated:
        if request.user.student is None:
            return redirect("/admin_panel/activity_list/")
        activity = Activity.objects.get(id=activity_id)
        path = os.path.join(os.getcwd(), 'static','sample.docx')
        
        doc = DocxTemplate(path)
        user = request.user.student
        data = {
            'activity_year' : activity.get_year_tw(),
            'number':user.id,
            'year': user.date_of_birth_tw()[0],
            'month':user.date_of_birth_tw()[1],
            'day': user.date_of_birth_tw()[2],
            'name': user.get_username(),
            'idnumber':user.identity,
            'address':user.address,
            'home_phone':user.home_phone,
            'mobile_phone':user.mobile_phone,
            'email':user.get_email(),
            'emergency_contact':user.emergency_contact,
            'emergency_contact_relationship':user.emergency_contact_relationship,
            'emergency_contact_phone':user.emergency_contact_phone,
            'education': user.get_education_display(),
            'military_service_number': user.military_service_number,
            'military_service':user.military_service,
            'military_rank':user.military_rank,
            'military_retired_year':user.date_of_military_retired_tw()[0],
            'military_retired_month':user.date_of_military_retired_tw()[1],
            'military_retired_day':user.date_of_military_retired_tw()[2],
            'military_service_years':user.get_military_service_years_display(),
            'identity_front':InlineImage(doc,user.identity_front.path, width=Mm(80)),   
            'identity_back':InlineImage(doc,user.identity_back.path, width=Mm(80)),

        }
        generate_docx(doc,data)
        generate_pdf(f'static/{data["number"]}.docx', 'static')
    # Create a FileResponse instance
        file_path = f'static/{data["number"]}.pdf'
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')

        # Set the Content-Disposition header to make the browser open the PDF viewer
        response['Content-Disposition'] = f'inline; filename={data["number"]}.pdf'

        # remove the file
        os.remove(f'static/{data["number"]}.docx')
        os.remove(file_path)
        return response
    else:
        return redirect("/student_login")
