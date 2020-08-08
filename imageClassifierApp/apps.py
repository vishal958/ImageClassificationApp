from django.apps import AppConfig
import joblib
import json
import os
from django.conf import settings


class ImageclassifierappConfig(AppConfig):
    name = 'imageClassifierApp'

    path = os.path.join(settings.MODELS, 'saved_model.pkl')
    path2 = os.path.join(settings.MODELS, 'class_dictionary.json')
    temp = 'Vishal'
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        model = joblib.load(pickled)
    with open(path2, 'r') as f:
        classdict = json.load(f)
       #data = pickle.load(pickled)
    model = model
    class_name_to_number = classdict
