from django.db import models
#from __future__ import unicode_literals
# Create your models here.

class Destination(models.Model):
    #id = int()
    name = models.CharField(max_length=100)
    desc = models.TextField()
    mark = models.IntegerField(default=11)

    def getdata(self):
        obj = Destination.objects.all()
        #obj = Destination.objects.get(id=1)
        return obj


class testing1(models.Model):
    userid = models.CharField(max_length=120,default="x")
    name = models.CharField(max_length=200)
    dob = models.DateField(default="2019-11-11")
    blood = models.CharField(max_length=200, default="O Positive")
    mobile = models.BigIntegerField(default=123)
    email = models.EmailField(default="aa@ddd")
    country = models.CharField(max_length=200, default="some country")
    state = models.CharField(max_length=200, default="some state")
    city = models.CharField(max_length=200, default="some city   ")
    emergency = models.CharField(max_length=10,  default="disagree")
    agree = models.BooleanField(default=False)
    donor = models.BooleanField(default=True)

    def getdata(self):
        obj = testing1.objects.all()
        return obj
    
    def auth(self,userid):
        obj = testing1.objects.filter(userid=userid).exists()
        return obj    

    def getreqdata(self, city, state, blood):
        obj = []
        obj = testing1.objects.all()

        
        O_neg = ["O Negative"]
        O_pos = ["O Negative","O Positive"]
        A_neg = ["O Negative","A Negative"]
        A_pos = ["O Positive","O Negative","A Negative","A Positive"]
        B_neg = ["O Negative","B Negative"]
        B_pos = ["O Positive","O Negative","B Positive","B Negative"]
        AB_neg = ["O Negative","B Negative","A Negative","AB Negative"]
        AB_pos = ["O Positive","O Negative","B Positive","B Negative","A Negative","A Positive","AB Positive", "AB Negative"]
        
        lst_O_pos = ["O Negative","O Positive"]
        #print(blood,"************")
        


        n = set()
        print(obj.filter(city=city, state=state).values(),"  \n")
        #print(n,"   ######")
        x = []
        if blood in "O Positive":
            for x in lst_O_pos:
                #print(x)
                #print(n)
                #n.objects.exclude()
                #x = obj.filter(city=city, state=state,blood=x)
                n.update(obj.filter(city=city, state=state,blood=x))
                #print(n)
                #obj = testing1.objects.all()
                #y = n | x
                #n = map(filtermtd, )
            else:
                return n
        
        if blood in "O Negative":
            for x in O_neg:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n

        
        if blood in "A Negative":
            for x in A_neg:            
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n
        
        if blood in "A Positive":
            for x in A_pos:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n

        
        if blood in "B Negative":
            for x in B_neg:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n
        
        if blood in "B Positive":
            for x in B_pos:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n
        
        if blood in "AB Negative":
            for x in AB_neg:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n
       
        if blood in "AB Positive":
            for x in AB_pos:
                n.update(obj.filter(city=city, state=state,blood=x))
            else:
                return n
        
class OrganDonors(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(default="2019-11-11")
    blood = models.CharField(max_length=200, default="O Positive")
    mobile = models.BigIntegerField(default=123)
    email = models.EmailField(default="aa@ddd")
    country = models.CharField(max_length=200, default="some country")
    donortype = models.CharField(max_length=200)
    organs1 = models.CharField(max_length=200)
    #organs2 = models.CharField(max_length=20)
    state = models.CharField(max_length=200, default="some state")
    city = models.CharField(max_length=200, default="some city   ")
    #emergency = models.BooleanField(default=False)
    agree = models.CharField(max_length=20, default="agree")
    #donor = models.BooleanField(default=True)

    def getdata(self):
        obj = OrganDonors.objects.all()
        return obj




