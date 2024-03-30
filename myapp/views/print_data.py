import subprocess
from django.contrib.auth.decorators import login_required
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from django.http import FileResponse
import os

def generate_pdf(doc_path, path):
    try:
        subprocess.call(['soffice',
                     '--headless',
                     '--convert-to',
                     'pdf',
                     '--outdir',
                     path,
                     doc_path])
    except Exception as e:
        print(f"生成 PDF 失敗: {e}")
        return None
    return doc_path
# soffice --convert-to pdf --outdir ./ ./sign_up_sample.docx

def generate_docx(doc_object,context,file_name):
    doc_object.render(context)
    doc_object.save(f'static/{file_name}.docx')
    
def file_response(file_name):
    file_path = f'static/{file_name}.pdf'
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')

    # Set the Content-Disposition header to make the browser open the PDF viewer
    response['Content-Disposition'] = f'inline; filename={file_name}.pdf'
    # remove the file
    os.remove(f'static/{file_name}.docx')
    os.remove(file_path)
    return response

