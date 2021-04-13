from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime

from datetime import date
from geoposition.fields import GeopositionField

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()


    def __str__(self):
        return self.name
# Create your models here.
class MyManager(BaseUserManager):

    def create_user(self, username,email, is_user=False,is_police=False, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")


        user = self.model(
            username=username
        )

        user.set_password(password)  # change password to hash
        user.is_sho=False
        user.email=email
        user.is_admin = False
        user.is_police = is_police
        user.is_user = is_user
        user.is_staff = False
        user.is_active = True

        return user
    def save(self, email,  password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")


        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)  # change password to hash


        user.is_admin = False
        user.is_police = False
        user.is_user = True
        user.is_staff = False
        user.is_active = True

        return user

    def create_superuser(self, username,  password,email):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")


        user = self.model(
            username=username
        )

        user.set_password(password)
        user.email=email
        user.is_admin = True
        user.is_police =False
        user.is_user = False
        user.is_staff=True
        user.is_active=True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class states(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.name


class city(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    state=models.ForeignKey(states,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MyUser(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(('email address'),unique=True,null=True,default="",blank=True)
    username=models.CharField(default="",max_length=15,unique=True)
    is_user = models.BooleanField(default=False)
    is_police = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_sho = models.BooleanField(default=False)
    entrydate= models.DateField(auto_now_add=True,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyManager()
    ref_key=models.CharField(default="",null=True,max_length=300,blank=True)
    def __str__(self):
        return self.username

class UserData(models.Model):
    user= models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    firstname=models.CharField(default="",max_length=10)
    middlename=models.CharField(default="",max_length=10)
    lastname=models.CharField(default="",max_length=10)
    dob= models.DateField(null=True, blank=True)
    gender=models.CharField(default="",max_length=11)
    m_status=models.CharField(default="",max_length=8)
    address=models.CharField(default="",max_length=200)
    state=models.ForeignKey(states,on_delete=models.CASCADE)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    pincode=models.IntegerField(default="")
    mobile_no=models.CharField(default="",max_length=10)
    passport_no=models.IntegerField(default="")
    aadhar_no=models.IntegerField(default="")
    aadhar_image=models.ImageField(upload_to="Fir_Project/media/Fir_app",default="")
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.firstname

class Police_Station_data(models.Model):
    sho=models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    station_name=models.CharField(default="",max_length=50)
    sho_fname=models.CharField(default="",max_length=20)
    sho_lname=models.CharField(default="",max_length=20)
    main_area = models.CharField(default="",max_length=100)
    state = models.ForeignKey(states, on_delete=models.CASCADE)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    pincode = models.IntegerField(default="")
    latitude = models.DecimalField(max_digits=30,decimal_places=10,blank=True,null=True,default=0.0)
    longitude = models.DecimalField(max_digits=30,decimal_places=10,blank=True,null=True,default=0.0)


    def __str__(self):
        return self.station_name

class Police_data(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    firstname = models.CharField(default="", max_length=10)
    middlename = models.CharField(default="", max_length=10)
    lastname = models.CharField(default="", max_length=10)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(default="", max_length=11)
    mobile_no = models.IntegerField(default="")
    passport_no = models.IntegerField(default="")
    aadhar_no = models.IntegerField(default="")
    duty_start_time=models.TimeField(default=datetime.datetime.now().time())
    duty_end_time=models.TimeField(default=datetime.datetime.now().time())
    sho_id = models.ForeignKey(Police_Station_data,on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname



class ContactU(models.Model):
    id=models.AutoField(primary_key=True)
    email = models.EmailField(('email address'))
    name = models.CharField(max_length=10,default="")
    msgs= models.CharField(max_length=300,default="")
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Fir(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    state = models.CharField(max_length=20,default="")
    city = models.CharField(max_length=20,default="")
    station=models.CharField(max_length=20,default="")
    sho_name=models.CharField(default="",max_length=100)
    crime_date=models.DateField()
    crime_time=models.TimeField()
    report_date=models.DateField(default=datetime.date.today)
    report_time=models.TimeField(default=datetime.datetime.now().time())
    crime_location=models.CharField(default="",max_length=300,blank=True,null=True)
    suspected_people=models.CharField(default="",max_length=300,blank=True,null=True)
    reasone_for_firdelay=models.CharField(default="",max_length=100,blank=True,null=True)
    stolen_things=models.CharField(default="",max_length=300,blank=True,null=True)
    stolen_amount=models.CharField(default=0.0,max_length=30,blank=True,null=True)

    additional_info=models.CharField(default="",max_length=800,blank=True,null=True)
    status=models.IntegerField(default=0)

    def __str__(self):
        return self.user.firstname


class Alerts(models.Model):
    user= models.ForeignKey(UserData,on_delete=models.CASCADE)
    main_area = models.CharField(max_length=100,default="")
    station = models.ForeignKey(Police_Station_data,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.firstname

