from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import authenticate
#from .models import Donor1
# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        
        state = request.POST.get('selctstate')
        city = request.POST.get('selectcity')
        bloodtype = request.POST.get('bloodtype')
        #d = Donor()
        #obj_list = []
        #obj_list = d.getdata()
        
        
        """
        for obj_list1 in obj_list:
            if obj_list1.state==state and obj_list1.city == city:
                
            else:
                return HttpResponse("not found")
        """
        #return render(request,"dashboard.html",{'obj_list':obj_list,'s':state,'c':city,'b':bloodtype})
        return render(request,"dashboard.html")

    else:
        return render(request,"dashboard.html")



def entry(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        bloodtype = request.POST.get('bloodtype')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        emergency = request.POST.get('emergency')
        agree = request.POST.get('agree')
        
        #d = Donor1()

    return render(request,"dashboard.html") 

    