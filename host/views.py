from django.shortcuts import render
from django.contrib.auth.models import  User, auth
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import authenticate
from .models import Hostuser, Hostcamp
# Create your views here.


def bloodcamp(request):
    #h = Hostuser()
    #hv = h.getdata()

    if request.method == 'POST':
        firstname = request.POST['first']
        lastname = request.POST['last']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if Hostuser.objects.filter(username=username).exists():
                print("Not created")
                return redirect("/host/bloodcamp")
            else:
                user = Hostuser(username=username,password=password1,email=email,firstname=firstname,lastname=lastname)
                user.save()
                return redirect("/host/bloodcamp")
        else:
            print("Password does Not matched")
            return redirect("/host/bloodcamp")
        

        print('user created')
        print('Username taken')
        print('Password did not matched.... ') 

    else:
        return render(request,"bloodcamp.html")



def auth3(request):
    if request.method == 'POST':
        username = request.POST['email_login']
        password = request.POST['password_login']

        h= Hostuser()
        #y = h.getdata()
        user = h.validateuser(username=username, password=password)
        
        if user is not None:
            #print("Authenticated user")
            return render(request,"hostprofile.html",{'name':username})
        else:
            #print("Not Authenticated user")
            return HttpResponse("Not a valid user or password is wrong")
    else:
        return redirect("/host/bloodcamp")
    

def entry(request):
    if request.method == 'POST':
        name = request.POST.get('frm2name')
        dob = request.POST.get('dob')
        blood = request.POST.get('bloodtype1')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        country = "India"
        state = request.POST.get('frm2state')
        city = request.POST.get('frm2city')
        emergency = request.POST.get('frm2campname')
        img = request.POST.get('hostimg')
        agree = True
        donor = True

        print(request.POST.get('emergency'))

        t = Hostcamp(name=name,dob=dob,blood=blood,mobile=contact,email=email,country=country,state=state,city=city,emergency=emergency,agree=agree,donor=donor)
        t.save()
        print(name)
        return render(request,"hostprofile.html")
    else:
        return HttpResponse("Hllo worlslcm")