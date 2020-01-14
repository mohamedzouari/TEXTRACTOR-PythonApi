from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import ImageModel

import json
import os, os.path
import glob

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def index(request):
    return JsonResponse("Hello, This is your Textractor API !")

@csrf_exempt 
def convert(request):
    if request.method == 'POST': 
        ImagePath = "C:/Users/Mohamed/Desktop/Projects/TEXTRACTOR/TextApi/TextractorProject/TextractorApi/images/"

        #save all files from the post to images folder
        fs = FileSystemStorage(location=ImagePath)

        for filename, file in request.FILES.items():
            name = request.FILES[filename].name
            filename = fs.save(name, request.FILES[filename])     
         

        # image conversion
        text =''

        for file in glob.glob( ImagePath +'*.*'):
            im=Image.open(file)
            text = text + pytesseract.image_to_string(im, lang="eng")
            os.remove(file)

        
        response = {'ConvertedText': text}
        return JsonResponse(response)

