from django.db import models
from datetime import date
# Create your models here.

class Hostcamp(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField(default="2019-11-11")
    blood = models.TextField(max_length=100, default="Any address")
    mobile = models.BigIntegerField(default=123)
    email = models.EmailField(default="aa@ddd")
    country = models.CharField(max_length=20, default="some country")
    state = models.CharField(max_length=40, default="some state")
    city = models.CharField(max_length=20, default="some city   ")
    emergency = models.TextField(default=100)
    agree = models.BooleanField(default=False)
    donor = models.BooleanField(default=False)
    #image = models.ImageField(upload_to="pics/")
    
    def getdata(self):
        today = date.today()
        print(today)
        print("#########")
        obj = Hostcamp.objects.filter(dob=today)
        #obj = Hostcamp.objects.all()      
        for x in obj:
            print(x.dob)
        return obj


class Hostuser(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    email = models.EmailField()

    def getdata(self):
        obj = Hostuser.objects.all()
        return obj

    def validateuser(self,username, password):
        obj1 = Hostuser.objects.all()
        n = obj1.filter(username=username, password=password).exists()
        if n is not None:
            return n
        else:
            return None
                

