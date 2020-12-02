from django.shortcuts import render,HttpResponse,redirect
import json
import hashlib,uuid
import os
from django.core import serializers
import random
import string
from django.contrib.auth.hashers import make_password,check_password
from sqlite3 import IntegrityError
from .app_settings import MY_SETTING
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db import transaction
from django.core.mail import send_mail,EmailMessage
from datetime import timedelta
# Create your views here.
def index(request):
    param={'victim':False,'police':False,'error':False,'sho':False}
    if request.session.has_key('victim'):
        param["victim"]= True
    elif request.session.has_key('police'):
        param["police"]= True
    elif request.session.has_key('sho'):
        param["sho"]= True

    return render(request,"Fir_app/index.html",param)

def signinpage(request):
    param={'signin':True,'signup':False}
    return render(request,"Fir_app/UserLogin.html",param)
@transaction.atomic
def signuppage(request):
    if request.method == "POST":
        uname=request.POST["uname"]
        fname= request.POST["fname"]
        mname= request.POST["mname"]
        lname= request.POST["lname"]
        dob= request.POST["dob"]
        gender= request.POST["radiogender"]
        m_status= request.POST["radiomaritalstatus"]
        address= request.POST["address"]
        state_id= request.POST["state"]
        state=states.objects.get(id=state_id)
        city_id= request.POST["city"]
        city1=city.objects.get(id=city_id)
        pincode= request.POST["pincode"]
        m_no= request.POST["mobileno"]
        passportno= request.POST["passportno"]
        aadharno= request.POST["aadharno"]
        email= request.POST["email"]
        password= request.POST["password"]
        image=request.FILES['file']
        user=MyUser.objects.create_user(username=uname,password=password,email=email,is_user=True)
        user.save()



        try:
            udata=UserData(user=user,firstname=fname,middlename=mname,lastname=lname,dob=dob,gender=gender,m_status=m_status,address=address,state=state,city=city1,pincode=pincode,mobile_no=m_no,passport_no=passportno,aadhar_no=aadharno,aadhar_image=image)
            udata.save()  # Could throw exception
        except IntegrityError:
            transaction.rollback()
        messages.success(request,"Successfully Registred")
        return redirect("Home")

    sts=states.objects.all()
    param = {'signin': False, 'signup': True,'states':sts}

    return  render(request,"Fir_app/UserRegistration.html",param)

def DashBoard_user(request):
    if request.session.has_key('victim'):
        sts = states.objects.all()
        param={'states':sts}
        print(sts)
        uid=request.session['victim']
        user=MyUser.objects.get(id=uid)
        udata=UserData.objects.get(user=user)

        cts=city.objects.filter(state=udata.state)
        my_firs = Fir.objects.filter(user=request.user.userdata)
        param['cities']=cts
        param['my_firs']=my_firs


        return render(request,"Fir_app/UserDashBoard.html",param)
    else:
        return redirect("Home")


def forgetpassword(request):
    if request.method == "POST":
        email=request.POST["email"]
        user = MyUser.objects.get(email=email)
        if user is None:
            messages.ERROR(request,"You are Not Registrade")
            return render(request, "Fir_app/forgetpassword.html")
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        refkey=make_password(result_str)

        uid=str(user.id)


        try:
            email = EmailMessage(
                subject="Forget Password",
                body=" http://127.0.0.1:8000/getpassword/?q=" + refkey+"&uid="+str(uid)+"\n Click On Above Link for Verification",
                from_email=MY_SETTING,
                to=[email],

            )
            messages.success(request, "Link Successfully Sent on your Email")
            email.send()
            user.ref_key=""
            user.ref_key=result_str
            user.save()
        except:
            messages.ERROR(request, "Something Went Wrong")

    return render(request,"Fir_app/forgetpassword.html")

def getpassword(request):
    if request.method == "POST":
        q = request.POST.get('key', '')
        uid = request.POST.get('uid', '')
        password=request.POST.get('pass', '')
        user=MyUser.objects.get(id=uid)

        if check_password(user.ref_key,q):
            print("Hello")
            user.password = ""
            user.password = make_password(password)
            user.save()
        else:
            messages.error(request,"Error")
            return render(request, "Fir_app/changepassword.html")
        messages.success(request, "Successfully Changed")
        return render(request, "Fir_app/changepassword.html")
    q=request.GET.get('q','')
    uid=request.GET.get('uid','')
    param={'key':q,'uid':uid}
    return render(request,"Fir_app/changepassword.html",param)
def fetch_city(request):
    state=request.GET["state"]
    state1=states.objects.get(id=state)
    print(state1)
    ct=city.objects.filter(state=state1)
    name=[]
    for c in ct:
        name.append({"name":c.name,"id":c.id})



    response1=json.dumps({"cities":name},default=str)

    return HttpResponse(response1)
def update_data(request,id):
    if request.method=="POST":
        print("Hello")
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        mname = request.POST["mname"]
        lname = request.POST["lname"]
        dob = request.POST["dob"]
        gender = request.POST["radiogender"]
        m_status = request.POST["radiomaritalstatus"]
        address = request.POST["address"]
        state = request.POST["state"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]
        m_no = request.POST["mobileno"]
        passportno = request.POST["passportno"]
        aadharno = request.POST["aadharno"]
        email = request.POST["email"]
        password = request.POST["password"]
        image=""
        if request.FILES.get('file') == None:
            image=""
        else:
            image = request.FILES['file']
        user=MyUser.objects.get(id=id)
        data = UserData.objects.get(user=user)
        user.email=email
        user.username=uname
        user.password=password
        user.save()
        data.firstname=fname
        data.middlename=mname
        data.lastname=lname
        data.dob=dob
        data.gender=gender
        data.m_status=m_status
        data.address=address
        data.state=state
        data.city=city
        data.pincode=pincode
        data.mobile_no=m_no
        data.passport_no=passportno
        data.aadhar_no=aadharno
        data.aadhra_image=image
        data.save()
        print(data)
        return redirect("user_Dash")

def DashBoard_sho(request):
    if request.session.has_key('sho'):
        id=request.session['sho']
        param={}
        polices= Police_data.objects.filter(sho_id=id)

        print(polices)
        param={"polices":polices}
        return render(request,"Fir_app/SHODashBoard.html",param)
    else:
        return redirect("Home")
def DashBoard_police(request):
    if request.session.has_key('police'):
        delta = timedelta(minutes=1)
       # end_time =request.user.police_data.duty_end_time

        end_time=datetime.datetime.strptime(str(request.user.police_data.duty_end_time), "%H:%M:%S") - timedelta(minutes=1)
        print(end_time.time())
        firs = Fir.objects.filter(report_time__gte = request.user.police_data.duty_start_time,report_time__lte=str(end_time.time()),station=request.user.police_data.sho_id)
        param={'my_firs':firs}
        print(firs)

        return render(request,"Fir_app/PoliceDashBoard.html",param)
    else:
        return redirect("Home")

def blockchain(request):
    return render(request,"Fir_app/Blockchain.html")

def contactus(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        msgs=request.POST["msg"]
        cot=ContactU(name=name,email=email,msgs=msgs)
        email = EmailMessage(
            subject=str(name)+"Want to say/ask",
            body=msgs,
            from_email=MY_SETTING,
            to=["harshpatel281199@gmail.com"],

        )
        email.send()
        cot.save()
        #send_mail(str(name)+"Want to say/ask", msgs,  email,["harshpatel281199@gmail.com"],
         #         fail_silently=False)
        messages.success(request,"Successfully Sent")
    return render(request,"Fir_app/contactus.html")
def emailcheck(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]
        uid= request.session["sho"]
        user=MyUser.objects.get(id=uid)
        user.email=email
        password=make_password(password)
        user.password=password
        user.save()

    return redirect("Home")
def loginprocess(request):
    if request.method=="POST":
        uname=request.POST['uname']
        loginpassword=request.POST['pass']
        print(uname)
        print(loginpassword)
        user=authenticate(username=uname,password=loginpassword)
        print(user)
        if user is not None:
            login(request,user)

            if user.is_user == True:
                request.session["victim"] = user.id
            elif user.is_police == True:
                request.session["police"] = user.id
            elif user.is_sho == True:
                if not user.email:
                    request.session["sho"] = user.id
                    return render(request,"Fir_app/checkemail.html")
                request.session["sho"] = user.id
            return redirect("Home")
        else:
            messages.error(request, "Invalid Credentials")
            return render(request,"Fir_app/UserLogin.html")
    return HttpResponse("404- Not Found")

def logoutprocess(request):
    logout(request)

    if request.session.has_key('victim'):
        del request.session['victim']
    if request.session.has_key('police'):
        del request.session['police']
    if request.session.has_key('sho'):
        del request.session['sho']

    return redirect("Home")

def save_police(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        mname = request.POST["mname"]
        lname = request.POST["lname"]
        dob = request.POST["dob"]
        gender = request.POST["radiogender"]
        m_no = request.POST["mobileno"]
        passportno = request.POST["passportno"]
        aadharno = request.POST["aadharno"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = MyUser.objects.create_user(username=uname,email=email,is_police=True,password=password)
        user.save()
        pd= Police_data(user=user,firstname=fname,middlename=mname,lastname=lname,dob=dob,gender=gender,mobile_no=m_no,passport_no=passportno,aadhar_no=aadharno)
        pd.save()


    return redirect("sho_dash")

def update_police(request,id):
    if request.method == "POST":
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        mname = request.POST["mname"]
        lname = request.POST["lname"]
        dob = request.POST["dob"]
        gender = request.POST["radiogender"]
        m_no = request.POST["mobileno"]
        passportno = request.POST["passportno"]
        aadharno = request.POST["aadharno"]
        email = request.POST["email"]
        password = request.POST["password"]
        user=MyUser.objects.get(id=id)
        pdata=Police_data(user=user)
        user.email=email
        user.username=uname
        user.password=password
        pdata.firstname=fname
        pdata.middlename=mname
        pdata.lastname=lname
        pdata.dob=dob
        pdata.gender=gender
        pdata.mobile_no=m_no
        pdata.passport_no=passportno
        pdata.aadhar_no=aadharno
        user.save()
        pdata.save()
        messages.success(request,"Success")
        print("Hello")

    return redirect("police_dash")



def firregistration(request):
    if request.session.has_key('victim'):
        if request.method == "POST":
            state_id = request.POST['state']
            city_id = request.POST['city']
            station_id = request.POST['police_station']
            sho = request.POST['sho_name']
            crime_date = request.POST['crime_date']
            crime_time = request.POST['crime_time']
            report_date = datetime.datetime.today().date()
            report_time = datetime.datetime.today().time()
            crime_location = request.POST['crime_loc']
            suspected_people = request.POST['suspected_people']
            reason_for_fir_delay = request.POST['reason_for_fir_delay']
            stolen_things = request.POST.get('stolen_things', '')
            stolen_amt = request.POST.get('stolen_amt', '')

            extra_points = request.POST.get('extra_points', '')
            state=states.objects.get(id=state_id)
            city1=city.objects.get(id=city_id)
            station=Police_Station_data.objects.get(sho__id=station_id)
            status = 0
            try:
                fir = Fir(user=request.user.userdata, state=state, city=city1, station=station, sho_name=sho,
                          crime_date=crime_date, crime_time=crime_time, report_date=report_date,
                          report_time=report_time, crime_location=crime_location, suspected_people=suspected_people,
                          reasone_for_firdelay=reason_for_fir_delay, stolen_things=stolen_things,
                          stolen_amount=float(stolen_amt),
                          additional_info=extra_points,status=status)
                fir.save()
                messages.success(request,"Your Fir is Successfully Registered")
            except:
                messages.error(request,"Somethong Went Wrong")

        sts = states.objects.all()
        today_date = datetime.datetime.today().date()

        current_time = datetime.datetime.now().time()

        return render(request, 'Fir_app/registerFIR.html',
                      {'states': sts, 'today_date': today_date, 'current_time': current_time})


def fetchstation(request):
    city=request.GET['city']
    stations = Police_Station_data.objects.filter(city=city)
    pts=[]
    for p in stations:
        pts.append({"name":p.station_name,"id":p.sho.id})



    response1=json.dumps({"stations":pts},default=str)

    return HttpResponse(response1)

def fetchsho(request):
    station = request.GET['station']
    st = Police_Station_data.objects.get(sho__id=station)
    sho=st.sho

    pts={"name": sho.username, "id": sho.id}

    response1 = json.dumps({"sho": pts}, default=str)

    return HttpResponse(response1)


def fetchfirdata(request):
    if request.session.has_key('victim'):
        id=request.GET['id']
        print(id)

        fir=Fir.objects.get(id=id)
        state=states.objects.get(id=fir.state.id)
        print(state)
        city1=city.objects.get(id=fir.city.id)
        station=Police_Station_data.objects.get(sho__id=fir.station.sho.id)
        fir=serializers.serialize('json',[fir,])

        resp=json.dumps({'msg':'success','fir':fir,'state':state.name,'city':city1.name,'station':station.station_name})
        return HttpResponse(resp)

    if request.session.has_key('police'):
        id=request.GET['id']
        print(id)

        fir=Fir.objects.get(id=id)
        state=states.objects.get(id=fir.state.id)
        print(state)
        city1=city.objects.get(id=fir.city.id)
        station=Police_Station_data.objects.get(sho__id=fir.station.sho.id)
        fir=serializers.serialize('json',[fir,])
        resp=json.dumps({'msg':'success','fir':fir,'state':state.name,'city':city1.name,'station':station.station_name})
        return HttpResponse(resp)


def sendtoblockchain(request):
    id=request.GET['id']
    try:
        fir=Fir.objects.get(id=id)
        fir.delete()
        resp=json.dumps({'msg':'success'})
        return HttpResponse(resp)
    except:
        resp=json.dumps({'msg':'failed'})
        return HttpResponse(resp)

