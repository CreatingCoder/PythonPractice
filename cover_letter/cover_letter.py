from docxtpl import DocxTemplate
from pathlib import Path


doc_path = Path(__file__).parent / 'template.docx'
doc = DocxTemplate(doc_path)

context = {
           'NAME': 'Shane',
           'ADR1' : '123 asdf drive',
           'ADR2' : 'Apt 123',
           'STATE' : 'MD',
           'CITY' : 'Hyattstown',
           'ZIP' : '21345',
           'PHONE': '123-234-3456',
           'EMAIL' : 'asdf@asdf.com'
           }

doc.render(context)
doc.save(Path(__file__).parent / 'letter.docx')
