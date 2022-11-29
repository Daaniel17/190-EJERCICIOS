import PyPDF2

pdf = open("Ejemplo.pdf", "rb")

reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extract_text())