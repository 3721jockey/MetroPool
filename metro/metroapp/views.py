from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from datetime import date,datetime,timedelta
import qrcode
from django.core.files.images import ImageFile


# Create your views here.

def index(request):
    return render(request,"index.html")

def chart(request):
    return render(request,"chart.html")

def bill(request):
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    fbid=request.GET.get("fid")
    fb=MetroBook.objects.get(id=fbid)
    iid = str(fb.id)
    data = iid + fb.start + "to" + fb.stop + fb.amount
    img = qrcode.make(data)
    fb.qr = data
    fb.save()
    img.save(f'C:\\PROJECT\\metro new\\metro\\metroapp\\static\\media\\QR\\{data}.png')
    
    


    
    return render(request,"bill.html",{"user":user,"fb":fb,"img":img})
def billw(request):
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    fbid=request.GET.get("id")
    fb=WaterBook.objects.get(id=fbid)
    iid = str(fb.id)
    data = iid + fb.start + "to" + fb.stop + fb.amount
    img = qrcode.make(data)
    fb.qr = data
    fb.save()
    img.save(f'C:\\LCC\\PROJECTS\\SCMS\\MetroPool\\metro\\metroapp\\static\\media\\QR\\{data}.png')
    
    


    
    return render(request,"billw.html",{"user":user,"fb":fb,"img":img})




def login(request):
    if request.POST:
        uname=request.POST["uname"]
        psw=request.POST["psw"]
        user=authenticate(username=uname,password=psw)
        
        print(user)
        if user:
            userdata=User.objects.get(username=uname)
            if userdata.is_superuser == 1:
                    return redirect("/adminHom")
            else:
                    messages.info(request,"Use Correct Login")

                    
            
        else:
            messages.info(request,"User dosent exist")
    return render(request,"login.html")

def loginCus(request):
    if request.POST:
        uname=request.POST["uname"]
        psw=request.POST["psw"]
        user=authenticate(username=uname,password=psw)
        
        print(user)
        if user:
            userdata=User.objects.get(username=uname)
            if userdata.is_superuser == 0:
                    request.session["email"]=uname
                    r = Registration.objects.get(email=uname)
                    request.session["id"]=r.id
                    request.session["name"]=r.name
                    return redirect("/userhome")           
            else:
                    messages.info(request,"Use Correct Login")


            
        else:
            messages.info(request,"User dosent exist")
    return render(request,"loginCus.html")


def register(request):
    if request.POST:
        name=request.POST["name"]
        con=request.POST["con"]
        email=request.POST["email"]
        add=request.POST["add"]
        psw=request.POST["psw"]
        user=Registration.objects.filter(email=email,psw=psw).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=User.objects.create_user(username=email,email=email,password=psw)
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Registration.objects.create(name=name,con=con,email=email,psw=psw,add=add,user=u)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request,"register.html")


def adminaddflights(request):
    if request.POST:
        name=request.POST["name"]
        
        img=request.FILES["img"]
        
        user=Flights.objects.filter(Name=name).exists()
        if user:
            messages.info(request,"Fight already exists")
        else:
            try:
                u=Flights.objects.create(Name=name,img=img)
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                messages.info(request,"Flight added successfully")
    return render(request,"adminaddflights.html")


def metroBook(request):
    no=datetime.now()
    n = no + timedelta(hours=2)
    n = n.time()
    print("**********")
    print(n)
    price = 0
    uid=request.session["id"]
    u=Registration.objects.get(id=uid)
    data=StopsM.objects.all()
    if request.POST:
        start=request.POST["start"]
        stop=request.POST["stop"]
        sta=StopsM.objects.get(id=start)
        sto=StopsM.objects.get(id=stop)
        diff=sto.id - sta.id
        diff = abs(diff)
        if diff == 1:
            price = 10
        elif diff == 2 or diff == 3 or diff == 4:
            price = 20
        elif diff == 5 or diff == 6 or diff == 7 :
            price = 30
        elif diff == 8 or diff == 9 or diff == 10 or diff == 11:
            price = 40
        elif diff == 12 or diff == 13 or diff == 14 or diff == 15 or diff == 16:
            price = 50
        
        elif diff == 17 or diff == 18 or diff == 19 or diff == 20 or diff == 21 or diff == 22 or diff == 23 or diff == 24:
            price = 60

        if price == 0:
            messages.info(request,"Choose stops correctly")
            return redirect("/metroBook")

        mB = MetroBook.objects.create(start=sta.stopname,stop=sto.stopname,amount=price,status="Active",user=u,time=n)
        mB.save()
        return redirect(f"/userpay?id={mB.id}")


    return render(request,"metroBook.html",{"data":data})

def waterBook(request):
    no=datetime.now()
    n = no + timedelta(hours=2)
    n = n.time()
    print("**********")
    print(n)
    price=0
    uid=request.session["id"]
    u=Registration.objects.get(id=uid)
    data=StopsW.objects.all()
    if request.POST:
        start=request.POST["start"]
        stop=request.POST["stop"]
        sta=StopsW.objects.get(id=start)
        sto=StopsW.objects.get(id=stop)
        diff=sto.id - sta.id
        diff = abs(diff)
        diff = abs(diff)
        
        if diff == 1:
            price = 10
        elif diff == 2 or diff == 3 or diff == 4:
            price = 20
        elif diff == 5 or diff == 6 or diff == 7 :
            price = 30
        elif diff == 8 or diff == 9 or diff == 10 or diff == 11:
            price = 40
        elif diff == 12 or diff == 13 or diff == 14 or diff == 15 or diff == 16:
            price = 50
        
        elif diff == 17 or diff == 18 or diff == 19 or diff == 20 or diff == 21 or diff == 22 or diff == 23:
            price = 60
        if price == 0:
            messages.info(request,"Choose stops correctly")
            return redirect("/waterBook")

        mB = WaterBook.objects.create(start=sta.stopname,stop=sto.stopname,amount=price,status="Active",user=u,time=n)
        mB.save()
        return redirect(f"/userwpay?id={mB.id}")
    return render(request,"waterBook.html",{"data":data})

def adminhome(request):


    return render(request,"adminhome.html")

def adminHom(request):
    p = Payment.objects.all()
    count = p.count()
    dt = date.today()
    dt = str(dt)
    d = dt[5:7]
    mSum = 0
 

    sum = 0
    for pi in p:
        sum = sum + pi.amt
        dte = str(pi.date)
        if dte == d:
            mSum = mSum + pi.amt
    
    return render(request,"adminHom.html",{"sum":sum, "mSum":mSum,"count":count})

def addService(request):
    data = Registration.objects.all()
    return render(request,"addService.html",{"data":data})




def addStation(request):
    data = StopsM.objects.get(id=1)
    data = StopsM.objects.all()
    if request.POST:
        stop = request.POST["stop"]
        s = StopsM.objects.create(stopname = stop)
        s.save()
        messages.info(request,"Station Added Successfully")
        return redirect("/adminHom")

    return render(request,"addStation.html",{"data":data})



def addWStation(request):
    data = StopsW.objects.all()
    if request.POST:
        stop = request.POST["stop"]
        s = StopsW.objects.create(stopname = stop)
        s.save()
        messages.info(request,"Station Added Successfully")
        return redirect("/adminHom")

    return render(request,"addWStation.html",{"data":data})

def schedulesMetro(request):
    if request.POST:
        name = request.POST["name"]
        time = request.POST["time"]
        type = request.POST["type"]
        s = Schedule.objects.create(mName = name,type  = type,time = time)
        s.save()
        messages.info(request,"Schedule Added Successfully")

        return redirect("/adminHom")

    return render(request,"schedulesMetro.html")

def adminpayment(request):
    data=Payment.objects.all()
    return render(request,"adminpayment.html",{"data":data})

def adminvbooking(request):
    data=FlightBook.objects.all()
    return render(request,"adminvbooking.html",{"data":data})


    return render(request,"adminseats.html",{"f":f,"se":se})



def upayment(request):
    return render(request,"upayment.html")

def feedBus(request):
    id=request.GET.get("id")
    return render(request,"feedBus.html",{"id":id})



def userpay(request):
    
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)

    mBid=request.GET.get("id")
    mB=MetroBook.objects.get(id=mBid)
   
    
 
    if request.POST:
        p=Payment.objects.create(mBid=mB,uid=user,amt=mB.amount)
        p.save()
     
        return redirect(f"/bill?fid={mB.id}")
    return render(request,"userpay.html",{"total":mB.amount})



def feederPay(request):
    mBid=request.GET.get("id")
    mB=MetroBook.objects.get(id=mBid)
    if request.POST:
        mB.srStatus = "FeederBus Booked"
        mB.save()
        return redirect("/userbooking")
    return render(request,"feederPay.html",{"total":mB.amount})

def poolPay(request):

    mBid=request.GET.get("id")
    mB=MetroBook.objects.get(id=mBid)

    if request.POST:
        mB.srStatus = "CarPool Booked"
        mB.save()
 
        return redirect("/userbooking")
    return render(request,"poolPay.html",{"total":mB.amount})

def cabPay(request):

    mBid=request.GET.get("id")
    mB=MetroBook.objects.get(id=mBid)

    if request.POST:
        mB.srStatus = "SingleCab Booked"
        mB.save()
  
        return redirect("/userbooking")
    return render(request,"cabPay.html",{"total":mB.amount})


def adminfood(request):
    data = FoodRequest.objects.all()
    return render(request,"adminfood.html",{"data":data})


def cabBook(request):
    id=request.GET.get("id")

    return render(request,"cabBook.html",{"id":id})

def schedule(request):
    data = Schedule.objects.all()
    return render(request,"schedule.html",{"data":data})

def bookFood(request):
    id=request.GET.get("id")
    status=request.GET.get("status")
    if status == "metro":
        mB=MetroBook.objects.get(id=id)
        stop=mB.stop
    else:
        wB=WaterBook.objects.get(id=id)
        stop=wB.stop
    if request.POST:
            req=request.POST["req"]

            fR=FoodRequest.objects.create(request=req,stop=stop)
            fR.save()
            return redirect("/userbooking")
    return render(request,"bookFood.html")

def userwpay(request):
    
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)

    mBid=request.GET.get("id")
    mB=WaterBook.objects.get(id=mBid)
   
    
 
    if request.POST:
        p=Payment.objects.create(wBid=mB,uid=user,amt=mB.amount)
        p.save()
        
        return redirect(f"/bill?fid={mB.id}")
    return render(request,"userwpay.html",{"total":mB.amount})





def userbooking(request):
    uid=request.session["id"]
    data=MetroBook.objects.filter(user__id=uid)

    dataw=WaterBook.objects.filter(user_id=uid)
    dte=date.today()
    now = datetime.now()
    no = now.time()
    print("******now time*****")
    print(no)



    for d in data:
        print (d.time)
        if no > d.time or dte > d.date:
            d.status = "Expired"
            d.save() 
    for de in dataw:
        if no > de.time or dte > de.date:
            de.status = "Expired"
            de.save() 

    return render(request,"userbooking.html",{"data":data,"dataw":dataw})

def adminbooking(request):
    data=MetroBook.objects.all()
    dataw=WaterBook.objects.all()

    dte = date.today()
    now = datetime.now()
    n=now.time()
    print("*********8")
    print(n)
    for d in data:
        if dte > d.date or n > d.time:
            d.status = "Expired"
            d.save() 
    for dw in dataw:
        if dte > dw.date or n > dw.time:
            dw.status = "Expired"
            dw.save() 
    

    return render(request,"adminbooking.html",{"data":data,"dataw":dataw})


def userpayment(request):
    uid=request.session["id"]
    data=Payment.objects.filter(uid__id=uid)
    
    return render(request,"upayment.html",{"data":data})



def userhome(request):
    return render(request,"userhome.html")





def uservflights(request):
    data=Schedule.objects.all()
    return render(request,"uservflights.html",{"data":data})









