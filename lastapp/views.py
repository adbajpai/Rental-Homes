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
        #####################################
        #response=render(request,"login.html",{'curl':curl})
        #response.set_cookie('email','renter')
        ####################################		
        #query="select * from majorprojectapp_destination where email='%s' and password='%s' " %(email,password)
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
############################################

"""
def verify_email(request):
    movies=z.renterimage.objects.filter()
    #info=z.renter.objects.filter()
    #details=z.renter.objects.filter(email=email)
    #details=z.renter.objects.filter()

    #val1=request.GET['num1'])
    #email=request.POST('email')
    #query="select * from renter_renter where email='%s'" %(email)
    #details=z.renter.objects.filter()

    #query="select * from renter_renter where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchone()

    #email=request.POST.get('email')
    #query="select * from renter_renterimage where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchall()

    #movies=z.renterimage.objects.filter()
    #info=z.renter.objects.filter()
    #############################
    #email=request.COOKIES.get('email')
    #############################
    if request.method=='POST':
        email = request.POST['email']

        if email:
            match = z.renter.objects.filter(Q(email=email))

            if match:
                return render(request,'profile.html',{'email':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/profile/')
            
    return render(request, "verify_email.html", {'curl':curl,'movies':movies,'media_url':media_url})

"""
"""
def profile(request):
    #movies=z.renterimage.objects.filter()

    
    #info=z.renter.objects.filter()
    #details=z.renter.objects.filter(email=email)
    #details=z.renter.objects.filter()

    #val1=request.GET['num1'])
    #email=request.POST('email')
    #query="select * from renter_renter where email='%s'" %(email)
    #details=z.renter.objects.filter()

    #query="select * from renter_renter where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchone()

    #email=request.POST.get('email')
    #query="select * from renter_renterimage where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchall()

    #movies=z.renterimage.objects.filter()
    #info=z.renter.objects.filter()
    #############################
    #email=request.COOKIES.get('email')
    #############################
    ##if request.method=='POST':
      ##  email = request.POST['email']

        ##if email:
            #match = z.majorprojectapp_destination.objects.filter(Q(email=email))
            #match = z.lastapp_destination.objects.filter(Q(email=email))
            #match = z.Destination.objects.filter(Q(email=email))
            #match = z.rentee.objects.filter(Q(email=email))
            #match = z.Destination.objects.filter(Q(email=email))
            ##match = z.Destination.objects.filter(Q(email=email))
            ##catch = z.rentee.objects.filter(Q(email=email))
            match = z.Destination.objects.filter(Q(email=request.session["uid"]))
            catch = z.rentee.objects.filter(Q(email=request.session["uid"]))
            #match = z.Destination.objects.filter(Q(email=email),name = request.session["uid"])
            
            if match:
                #return render(request,'profile.html',{'email':match})
                
                return render(request,'profile.html',{'email':match,'fmail':catch,'udata':request.session["uid"]})
                #return render(request,'profile.html',{'udata':request.session["uid"]})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/profile/')
            
    #return render(request, "verify_email.html", {'curl':curl,'movies':movies,'media_url':media_url})
    ##return render(request, "verify_email.html", {'curl':curl,'media_url':media_url})
    return render(request, "profile.html", {'curl':curl,'udata':request.session["uid"]})    
##########################################################################################################################33
"""
def profile(request):    
    match = z.Destination.objects.filter(Q(email=request.session["uid"]))
    catch = z.rentee.objects.filter(Q(email=request.session["uid"]))
    #ratch = z.renter.objects.filter(Q(email=request.session["uid"]))
    return render(request,'profile.html',{'email':match,'fmail':catch,'udata':request.session["uid"]})       
##########################################################################################################################33

def rentersearch(request):
    #movies=z.renterimage.objects.filter()

    
    #info=z.renter.objects.filter()
    #details=z.renter.objects.filter(email=email)
    #details=z.renter.objects.filter()

    #val1=request.GET['num1'])
    #email=request.POST('email')
    #query="select * from renter_renter where email='%s'" %(email)
    #details=z.renter.objects.filter()

    #query="select * from renter_renter where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchone()

    #email=request.POST.get('email')
    #query="select * from renter_renterimage where email='%s'" %(email)
    #models.cursor.execute(query)
    #details=models.cursor.fetchall()

    #movies=z.renterimage.objects.filter()
    #info=z.renter.objects.filter()
    #############################
    #email=request.COOKIES.get('email')
    #############################
    if request.method=='POST':
        email = request.POST['email']

        if email:
            #match = z.majorprojectapp_destination.objects.filter(Q(email=email))
            #match = z.lastapp_destination.objects.filter(Q(email=email))
            #match = z.Destination.objects.filter(Q(email=email))
            #match = z.rentee.objects.filter(Q(email=email))
            #match = z.Destination.objects.filter(Q(email=email))
            #match = z.Destination.objects.filter(Q(email=email))
            #catch = z.rentee.objects.filter(Q(email=email))
            fatch = z.renter.objects.filter(Q(email=email))
            
            if fatch:
                #return render(request,'profile.html',{'email':match})
                return render(request,'rentersearch.html',{'zmail':fatch})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/rentersearch/')
            
    #return render(request, "verify_email.html", {'curl':curl,'movies':movies,'media_url':media_url})
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

#    movies=z.renterimage.objects.filter()

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
        #p=models.renter(name=name,email=email,phone_number=phone_number,mobile_number=mobile_number,state=state,city=city,locality=locality,house_number=house_number,landmark=landmark,
        #               no_of_rooms=no_of_rooms,kitchen=kitchen,bathroom=bathroom,location=location,message=message,rent_value=rent_value,electricity_charge=electricity_charge,water_charge=water_charge)
        #pica=request.FILES['pica']
        #picb=request.FILES['picb']
        #picc=request.FILES['picc']
        #fs = FileSystemStorage()
        #filenamea = fs.save(pica.name,pica)
        #filenameb = fs.save(picb.name,picb)
        #filenamec = fs.save(picc.name,picc)
        #p=models.addcat(pic1=filename1)
        #p=models.addcat(pic2=filename2)
        #p=models.addcat(pic3=filename3)
        p=models.renter(name=name,email=email,phone_number=phone_number,mobile_number=mobile_number,state=state,city=city,locality=locality,house_number=house_number,landmark=landmark,
                        no_of_rooms=no_of_rooms,kitchen=kitchen,bathroom=bathroom,location=location,message=message,rent_value=rent_value,electricity_charge=electricity_charge,water_charge=water_charge)

        p.save()
        myurl=curl+'profile/?output=Register successfully'	
        return redirect(myurl)
   
def logout(request):
#    del request.session['uid']
    return redirect('/login')




























