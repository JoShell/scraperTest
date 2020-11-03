import PyPDF2
import os

pdfFile = open('meetingminutes1.pdf', 'rb') # open file in current directory and rb is read binary, as pdf is binary
 
reader = PyPDF2.PdfFileReader(pdfFile) # take the pdfFile object created about, assign it a variable name and pass it to the reader function

noPage = reader.numPages # assign a variable name to the object number of pages function

print(noPage) # print the number of pages in the termainal

page = reader.getPage(0) # assign page variable to the reader.getPage object generated for the first page (o) argument
exText = page.extractText() # creating the page object above, now use the method to extract text and then assign that to the new variable/object exText
print(exText) # print the text from the exText object - page 0

for pageNum in range(noPage): # for i, in the range variable object noPage created above
    print(reader.getPage(pageNum).extractText()) # reader gets one page at a time, extracts the text and then prints it

