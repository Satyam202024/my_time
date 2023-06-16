# Import the convert method from the
# docx2pdf module
from docx2pdf import convert
from pdf2image import convert_from_path
# for converting docs to pdf files
convert("example.docx")
convert("extra_project\example.docx", "extra_project\Mine.pdf")



#for converting pdf to image files
images = convert_from_path('example.pdf')
for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
