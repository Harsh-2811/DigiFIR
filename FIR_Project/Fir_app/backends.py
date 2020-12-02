from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import MyUser

class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            myuser = MyUser.objects.get(username=username)

            print("password ",myuser.password)
            if myuser.password == password:
                return myuser
        except :
            pass