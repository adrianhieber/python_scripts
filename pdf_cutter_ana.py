from PyPDF2 import PdfFileWriter, PdfFileReader

name = "Skript-Analysis_III.pdf"  # input("Name: ")+".pdf"
pages = int(input("seiten weglassen: "))

inputpdf = PdfFileReader(open(name, "rb"))

output = PdfFileWriter()

for i in range(pages, inputpdf.numPages):
    output.addPage(inputpdf.getPage(i))

with open(f"{name.rstrip('.pdf')}_teiler.pdf", "wb") as outputStream:
    output.write(outputStream)
