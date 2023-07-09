'''from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings


def save_pdf(params:dict):
    template=get_template("pdf.html")
    html=template.render(params)
    response=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    file_name=uuid.uuid4()

    try:
        with open(str(settings.BASE_DIR)+f'/media/{file_name}.pdf','wb+') as output:
             pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),output)

    except Exception as e:
        print(e)
    if pdf.err:
        return ' ',False
    return file_name,True'''

from io import BytesIO
from django.conf import settings
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
import uuid as u

def save_pdf(params:dict):
    template=get_template("pdf.html")
    html=template.render(params)
    response=BytesIO()
    file_name=u.uuid4()
    pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)

    try:
        with open(f'/media/{file_name}.pdf','wb+') as output:
            pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),output)

    except Exception as e:
        print(e)
    
    if pdf.err:
        return ' ',False
    return file_name,True