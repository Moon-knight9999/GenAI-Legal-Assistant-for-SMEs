from reportlab.platypus import SimpleDocTemplate, Paragraph

def export_pdf(text, path):
    doc = SimpleDocTemplate(path)
    doc.build([Paragraph(text)])
