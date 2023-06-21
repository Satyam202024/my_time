# Import the convert method from the
# docx2pdf module
# from docx2pdf import convert
# from pdf2image import convert_from_path
# for converting docs to pdf files
# convert("example.docx")
# convert("extra_project\example.docx", "extra_project\Mine.pdf")



# #for converting pdf to image files
# images = convert_from_path('example.pdf')
# for i in range(len(images)):
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')

import os
import win32com.client
import time


wdFormatPDF = 17

in_file=r'C:\Users\satyam\OneDrive\Desktop\my_time\extra_project\MT2.docx'
out_file=r'C:\Users\satyam\OneDrive\Desktop\my_time\extra_project'



# create COM object
word = win32com.client.Dispatch('Word.Application')
word.Visible = True
time.sleep(3)

# convert docx file 1 to pdf file 1
doc=word.Documents.Open(in_file) # open docx file 1
doc.SaveAs(out_file, FileFormat=wdFormatPDF) # conversion
doc.Close() # close docx file 1
word.Visible = False
word.Quit() # close Word Application 

from PyPDF2 import PdfReader

reader = PdfReader(r"C:\Users\satyam\OneDrive\Desktop\my_time\extra_project.pdf")
time.sleep(10)

page = reader.pages[0]
count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1
