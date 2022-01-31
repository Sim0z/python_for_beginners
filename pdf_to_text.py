import PyPDF2

pdf_object = open(r"C:\Users\user\OneDrive\Desktop\test.pdf", 'rb')

#create a reader for the file
pdf_reader = PyPDF2.PdfFileReader(pdf_object)

#store the number of pages in this PDf
x = pdf_reader.getPage(0)

print(x.extractText())

pdf_object.close()


