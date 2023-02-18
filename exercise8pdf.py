from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

files=[file for file in 
os.listdir() 
if file.endswith('.pdf') ]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

# import pypdf
# pdfFileObj = open('100DaysPython/demo/Mrinal_Nptel.pdf', 'rb')
# readpdf = pypdf.PdfReader(pdfFileObj) #read the page from pdf 
# print(len(readpdf.pages)) #print the number of page
# # page=list(pdfFileObj)
# for i in page:
#     print(i)
# # print(page.extract_text())

