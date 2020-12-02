from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
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
admin.site.register(Police_Station_data,station_data)

admin.site.register(Police_data)
admin.site.register(states)
admin.site.register(city)

admin.site.register(Fir)
admin.site.site_header = "DigiFIR Admin"
admin.site.site_title = "DigiFIR Admin Portal"