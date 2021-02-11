from datetime import datetime
from django.conf import settings
import django
import sys
from django.http.request import HttpRequest
sys.path.insert(0, 'D:/Django/DigiFIR/FIR_Project')
sys.path.insert(0, 'D:/Django/DigiFIR/FIR_Project/FIR_Project')

from FIR_Project.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()
from FIR_Project.settings import  SESSION_ID
from Fir_app.models import dummy_fir

print(SESSION_ID)

def save_fir(first_name,middle_name,surname,dob,crime_type):
    dfir = dummy_fir()
    dfir.first_name = first_name
    dfir.middle_name = middle_name
    dfir.last_name = surname
    dob1 = datetime.strptime(dob, "%d/%m/%Y").strftime("%Y-%m-%d")
    dfir.dob = dob1
    dfir.type = crime_type
    dfir.save()
    print(first_name)

    return
