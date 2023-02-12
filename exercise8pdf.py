import pypdf
pdfFileObj = open('100DaysPython/demo/Mrinal_Nptel.pdf', 'rb')
readpdf = pypdf.PdfReader(pdfFileObj) #read the page from pdf 
print(len(readpdf.pages)) #print the number of page
# page=list(pdfFileObj)
# for i in page:
#     print(i)
# # print(page.extract_text())
