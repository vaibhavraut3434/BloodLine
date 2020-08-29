from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import authenticate
from .models import Destination
from .models import testing1
from .models import OrganDonors

# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first']
        lastname = request.POST['last']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Not created")
                return HttpResponse('User not created.. Username already Exist.')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                return redirect("/accounts/fashion")
        else:
            print("Password does Not matched")
            return HttpResponse('Password does Not matched')
        

        print('user created')
        print('Username taken')
        print('Password did not matched.... ') 

    else:
        return render(request,"fashion.html")


def auth2(request):    
    if request.method == 'POST':
        username = request.POST['email_login']
        password = request.POST['password_login']

        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            #print("Authenticated user")
            return render(request,"dashboard.html",{"username1x":username})
        else:
            #print("Not Authenticated user")
            return HttpResponse("Not a valid user or password is wrong")
    else:
        return redirect("/accounts/fashion")

def fetch():
    obj = "vaibhav"
    return obj



def dashboard(request):
    if request.method == 'POST':
        
        state = request.POST.get('selctstate')
        city = request.POST.get('selectcity')
        bloodtype = request.POST.get('selectbloodtype')
        d = testing1()
        
        #print(bloodtype)
        
        obj_list = d.getreqdata(city,state,bloodtype)
        #new_obj = obj_list.filter(city=city,state=state,blood=bloodtype)
        #print(obj_list)
        

        """
        for obj_list1 in obj_list:
            if obj_list1.state==state and obj_list1.city == city:
                
            else:
                return HttpResponse("not found")
        """
        return render(request,"dashboard.html",{'obj_list':obj_list,'s':state,'c':city,'b':bloodtype})
        #return render(request,"dashboard.html")

    else:
        return render(request,"dashboard.html")


def entry(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        is_updated_form = request.POST.get('is_updated_form')
        name = request.POST.get('frm2name')
        dob = request.POST.get('dob')
        blood = request.POST.get('bloodtype1')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        country = "India"
        state = request.POST.get('frm2state')
        city = request.POST.get('frm2city')
        emergency = request.POST.get('emergency')
        agree = True
        donor = True

      
        #print(request.POST.get('emergency'))
        t_obj = testing1()
        user = t_obj.auth(userid)
        
        
        #change emergency

        if is_updated_form != None:
            print(user,"!!!!!!!!!!!!!!!!!!!!!!!!!!!",is_updated_form)
            testing1.objects.filter(userid=is_updated_form).update(userid=is_updated_form, name=name,dob=dob,blood=blood,mobile=contact,email=email,country=country,state=state,city=city,emergency='emergency',agree=agree,donor=donor)


        if user is False:
            #print("##################")
            t = testing1(userid=userid, name=name,dob=dob,blood=blood,mobile=contact,email=email,country=country,state=state,city=city,emergency='emergency',agree=agree,donor=donor)
            t.save()
            return render(request,"dashboard.html",{"user_updated_id":userid})
        else:
            return render(request,"dashboard.html",{"user_updated_id":userid})

        
        #print(name, dob)
    else:
        return HttpResponse("Hllo worlslcm")
        


def orgform(request):
    organsx = "xx"
    if request.method == 'POST':
        name = request.POST.get('orgname')
        dob = request.POST.get('orgdob')
        blood = request.POST.get('orgbloodtype1')
        contact = request.POST.get('orgcontact')
        email = request.POST.get('orgemail')
        country = "India"
        donortype = request.POST.get('donortype')

        #organsx = request.POST.get('liveorgan')
        #organs2 = request.POST.get('deadorgan')
        state = request.POST.get('orgfrm2state')
        city = request.POST.get('orgfrm2city')
        #emergency = True
        agree = request.POST.get('orgagree')
        #donor = True
        #print(name)
        
        #print(donortype)
        #print("donortype datatype")
        type(donortype)
        
        if donortype in "Live Donor":
            #print(donortype,"$$$$$$$$$$$$$$")
            organsx = request.POST.get('liveorgan')
            #print(organsx,"!!!!!!!!!!!!!!!")
        
        if donortype in "Brain Dead":
            organsx = request.POST.get('deadorgan')
            #print(organsx,"@@@@@@@@@@@@@@@")
        
        #print(organsx,"#########")
        o = OrganDonors(name=name,dob=dob,blood=blood,mobile=contact,email=email,country=country,donortype=donortype,organs1=organsx,state=state,city=city,agree=agree)
        
        #print(o.blood)
        #print(o.donortype)
        
        o.save()
        #obj = o.getdata()


        #for x in obj:
        #    print(x.name)

        
        #return redirect("/")

        return render(request,"dashboard.html")
    else:
        return HttpResponse("Not a Post method")



def organdata(request):
    obj = OrganDonors()
    obj_list2 = []
    obj_list2 = obj.getdata()

    for x in obj_list2:
        print(x.name,"#####################")
    return render(request,"dashboard.html",{'obj_list2':obj_list2}) 

