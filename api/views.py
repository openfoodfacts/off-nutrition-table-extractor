from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import UploadFileForm
import cv2
import json
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'nutrition_extractor'))
sys.path.append(os.path.join(os.getcwd(), 'nutrition_extractor/data'))
from detection import detect
@csrf_exempt

def nutritionExtract(request):
	if request.method == 'POST':
		new_file = UploadFile(file = request.FILES['image'])
		new_file.save()
		name = new_file.file.name
		response = detect(name, False)
		return JsonResponse(response)
