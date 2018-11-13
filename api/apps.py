from django.apps import AppConfig
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'nutrition_extractor'))
import detection as detect
import text_detection as text_detect

class ApiConfig(AppConfig):
    name = 'api'
    def ready(self):
        detect.load_model()
        text_detect.load_text_model()
