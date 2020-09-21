from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth.models import auth
from .import models
from lastapp import models as z
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

curl= settings.CURRENT_URL
media_url=settings.MEDIA_URL


def home(request):
    return render(request, "home.html", {})

def register(request):
    if request.method=='GET':
        if request.GET.get('output')==None:
            output=""
        else:
            output=request.GET.get('output')	
        return render(request,"register.html",{'curl':curl,'output':output})
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            p=models.Destination(name=name,email=email,password=password1)
            p.save()
            myurl=curl+'login/?output=Register successfully'	
            return redirect(myurl)
        else:
            print("password not matching......")
            myurl=curl+'register/'	
            return redirect(myurl)

def login(request):
    if request.method=="GET": 
        return render(request,'login.html',{'curl':curl,'output':''})
    else:
        email=request.POST.get('email')	
        password=request.POST.get('password')
        ####################################		
        query="select * from lastapp_destination where email='%s' and password='%s' " %(email,password)
        models.cursor.execute(query)
        userDetails=models.cursor.fetchall()
###########################################
        if len(userDetails)>0:
            request.session['uid']=request.POST["email"]
            return redirect(curl+'profile/')
            print("user login")
        else:	
            return redirect(curl+'register/')
            print("please check your password and try again")
        if request.session.has_key('uid'):
            s = Register.object.all()
            return render(request,'register.html',{'curl':curl,'output':'Login failed invalid user or verify your account'})				
        else:
            return redirect('login')
###########################################
def profile(request):    
    match = z.Destination.objects.filter(Q(email=request.session["uid"]))
    catch = z.rentee.objects.filter(Q(email=request.session["uid"]))
    #ratch = z.renter.objects.filter(Q(email=request.session["uid"]))
    return render(request,'profile.html',{'email':match,'fmail':catch,'udata':request.session["uid"]})       
##########################################################################################################################33

def rentersearch(request):
    if request.method=='POST':
        email = request.POST['email']

        if email:
            fatch = z.renter.objects.filter(Q(email=email))
            
            if fatch:
                #return render(request,'profile.html',{'email':match})
                return render(request,'rentersearch.html',{'zmail':fatch})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/rentersearch/')
            
    
    return render(request, "verify_renter.html", {'curl':curl,'media_url':media_url})


############################################################################################################################


def search(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = z.renter.objects.filter(Q(city__icontains=srch))

            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
        
    return render(request,"search.html", {})

def rentee(request):
    if request.method=='GET':
        if request.GET.get('output')==None:
            output=""
        else:
            output=request.GET.get('output')	
        return render(request,"rentee.html",{'curl':curl,'output':output})
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        mobile_number=request.POST.get('mobile_number')
        occupation=request.POST.get('occupation')
        maritial_status=request.POST.get('maritial_status')
        family_member=request.POST.get('family_member')
        p=models.rentee(name=name,email=email,phone_number=phone_number,mobile_number=mobile_number,
                        occupation=occupation,maritial_status=maritial_status,family_member=family_member)
        p.save()
        myurl=curl+'profile/?output=Register successfully'	
        return redirect(myurl)


def renter(request):
    if request.method=='GET':
        if request.GET.get('output')==None:
            output=""
        else:
            output=request.GET.get('output')	
        return render(request,"renter.html",{'curl':curl,'output':output})
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        mobile_number=request.POST.get('mobile_number')
        state=request.POST.get('state')
        city=request.POST.get('city')
        locality=request.POST.get('locality')
        house_number=request.POST.get('house_number')
        landmark=request.POST.get('landmark')
        no_of_rooms=request.POST.get('no_of_rooms')
        kitchen=request.POST.get('kitchen')
        bathroom=request.POST.get('bathroom')
        location=request.POST.get('location')
        message=request.POST.get('message')
        rent_value=request.POST.get('rent_value')
        electricity_charge=request.POST.get('electricity_charge')
        water_charge=request.POST.get('water_charge')
        p=models.renter(name=name,email=email,phone_number=phone_number,mobile_number=mobile_number,state=state,city=city,locality=locality,house_number=house_number,landmark=landmark,
                        no_of_rooms=no_of_rooms,kitchen=kitchen,bathroom=bathroom,location=location,message=message,rent_value=rent_value,electricity_charge=electricity_charge,water_charge=water_charge)

        p.save()
        myurl=curl+'profile/?output=Register successfully'	
        return redirect(myurl)
   
def logout(request):
    return redirect('/login')




























