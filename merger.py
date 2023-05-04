import os
from PyPDF2 import PdfWriter

toadd = open("eval.pdf", "rb")

for (dirpath, dirnames, filenames) in os.walk("."):
	for filename in filenames:
		if ".pdf" not in filename or filename=="eval.pdf":
			continue
			
		os.chdir(dirpath)
		
		inputpdf = open(filename, "rb")
		output = PdfWriter()
		
		output.append(toadd)
		output.append(inputpdf)
		
		output.write(filename)
		output.close()
