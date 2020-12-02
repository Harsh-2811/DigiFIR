from . import  views
from django.urls import path

urlpatterns = [
    path("",views.index,name="Home"),
    path("blockchain/",views.blockchain,name="Bc"),
    path("loginprocess/",views.loginprocess,name="lg"),
    path("signin/",views.signinpage,name="Signin"),
    path("signup/",views.signuppage,name="Signup"),
    path("fetchcity/",views.fetch_city,name="FetchCity"),
    path("fetchstation/",views.fetchstation,name="fetchstation"),
    path("fetchsho/",views.fetchsho,name="fetchsho"),
    path("forgetpassword/",views.forgetpassword,name="forgetpassword"),
    path('getpassword/',views.getpassword,name="getpassword"),
    path("updatedata/<int:id>",views.update_data,name="update"),
    path("update_police/<int:id>",views.update_police,name="update_police"),
    path("dashboard_user/",views.DashBoard_user,name="user_Dash"),
    path("dashboard_sho/",views.DashBoard_sho,name="sho_dash"),
    path("dashboard_police/",views.DashBoard_police,name="police_dash"),
    path("savepolice/",views.save_police,name="policedata"),
    path("contactus/",views.contactus,name="contact"),
    path("logout/",views.logoutprocess,name="contact"),
    path("emailchecking/",views.emailcheck,name="emailcheck"),
    path("firregistration/",views.firregistration,name="firregistration"),
    path("fetchfirdata/",views.fetchfirdata,name="fetchfirdata"),
    path("sendtoblockchain/",views.sendtoblockchain,name="sendtoblockchain"),

]