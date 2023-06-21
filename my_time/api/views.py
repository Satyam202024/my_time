from django.shortcuts import render
from .models import Upload
from .serializer import UpoadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import win32com.client
import pythoncom
import time
# .env.json
import pdb
from PyPDF2 import PdfReader
class UploadView(APIView):
    def post(self, request):
        serializer = UpoadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data['file'])
            # pdb.set_trace() 
            doc_file = serializer.data['file']
            # print(doc_file.name)
            in_file =r'C:\Users\satyam\OneDrive\Desktop\my_time\my_time'+ doc_file
            # print(do)
            # print(r'C:\Users\satyam\OneDrive\Desktop\my_time\my_time'+ in_file)
            out_file = r'C:\Users\satyam\OneDrive\Desktop\my_time\my_time\documents\documents'
            
            wdFormatPDF = 17

            pythoncom.CoInitialize()  # Initialize the COM library

            word = win32com.client.Dispatch('Word.Application')
            word.Visible = True
            time.sleep(3)

            doc = word.Documents.Open(in_file)
            time.sleep(10)
            # doc.saveAs(out_file, FileFormat=wdFormatPDF)
            doc.SaveAs(out_file, FileFormat=wdFormatPDF, AddToRecentFiles=True)
            doc.Close()
            word.Visible = False
            word.Quit()

            pythoncom.CoUninitialize()  # Uninitialize the COM library
            print(out_file)
            out_file=out_file+'.pdf'
            reader = PdfReader(out_file)
            time.sleep(10)
            page = reader.pages[0]
            count = 0

            for image_file_object in page.images:
                with open(str(count) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                    count += 1
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
