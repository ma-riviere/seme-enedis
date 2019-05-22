from docx import Document

def concat(tweet):
    return '.||'.join([i for i in tweet])

def write2docx(input):
    document = Document()
    document.add_paragraph(input)
    document.save('to_translate.docx')