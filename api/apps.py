from django.apps import AppConfig
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'nutrition_extractor'))
import detection as detect

class ApiConfig(AppConfig):
    name = 'api'
    def ready(self):
    	detect.load_model()
