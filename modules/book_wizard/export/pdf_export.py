from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def export_as_pdf(title, text):
    filename = f"public/exports/{title.replace(' ', '_')}.pdf"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    textobject = c.beginText(40, height - 40)
    for line in text.split('\n'):
        textobject.textLine(line)
    c.drawText(textobject)
    c.save()
    return filename
