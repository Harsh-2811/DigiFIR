
from django.conf import settings
import django

from FIR_Project.FIR_Project.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
INSTALLED_APPS.insert(0,'FIR_Project.Fir_app')
INSTALLED_APPS.remove('Fir_app')

django.setup()

from FIR_Project.Fir_app.models import *

def Hello():
    print(Fir.objects.all())