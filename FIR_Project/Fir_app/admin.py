from django.contrib import admin
from django.conf import settings
from .models import *
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
import requests

URL = "https://geocode.search.hereapi.com/v1/geocode"


class myUserModel(ModelAdmin):
    list_display = ['username','email','is_police','is_sho','is_admin','is_user']
admin.site.register(MyUser,myUserModel)
class userdatamodel(ModelAdmin):
    list_display = ['firstname','lastname','dob','gender','m_status','mobile_no','passport_no','aadhar_no','aadhar_image']
admin.site.register(UserData,userdatamodel)
class contactmodel(ModelAdmin):
    list_display = ['email','name','msgs','date']
admin.site.register(ContactU,contactmodel)

class station_data(ModelAdmin):
    list_display = ['station_name','sho_fname','sho_lname','state','city','pincode']


    def save_model(self, request, obj, form, change):
        location = str(obj.main_area) + " "+ str(obj.city) + str(obj.state)
        api_key = 'Sjbs1jct2RbI-1oyW7G9ow6fJBglVWeUaizszl26Q_E'  # Acquire from developer.here.com
        PARAMS = {'apikey': api_key, 'q': location}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()

        obj.latitude = data['items'][0]['position']['lat']
        obj.longitude = data['items'][0]['position']['lng']
        super().save_model(request, obj, form, change)



admin.site.register(Police_Station_data,station_data)

admin.site.register(Police_data)
admin.site.register(states)
admin.site.register(city)


class FirAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    change_list_template = 'admin/change_list_graph.html'

admin.site.register(Fir,FirAdmin)


"""
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'language', 'grades', 'gender')
    list_filter = ('language', 'gender', 'grades')
    save_as = True
    save_on_top = True
    change_list_template = 'admin/change_list_graph.html'
"""
admin.site.register(Alerts)
#admin.site.register(Student, StudentAdmin)
admin.site.site_header = "DigiFIR Admin"
admin.site.site_title = "DigiFIR Admin Portal"