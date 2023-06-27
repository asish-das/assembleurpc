from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
from django.db.models import Q

######################################################################
#                           LOAD INDEX PAGE
######################################################################


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "index.html")
######################################################################
#                           LOGIN
######################################################################


def login(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        user = authenticate(username=email, password=pwd)
        if user is not None:

            request.session['email'] = email
            if user.is_active:
                if user.is_superuser:
                    return HttpResponseRedirect("/adminhome")
                elif user.is_staff:
                    data = Courier.objects.get(email=email)
                    request.session['uid'] = data.id
                    return HttpResponseRedirect("/courierhome")
                else:
                    data = Customer.objects.get(email=email)
                    request.session['uid'] = data.id
                    return HttpResponseRedirect("/customerhome")
            else:
                msg = "You are not authenticated to login"
        else:
            msg = "User doesnt exist"
    return render(request, "commonlogin.html", {"msg": msg})
######################################################################
#                      REGISTRATION
######################################################################


def register(request):
    """ 
        The function to load customer registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]
        pin = request.POST["txtPin"]
        try:
            user = User.objects.create_user(username=email, password=pwd)
            user.save()
            cust = Customer.objects.create(
                name=name, email=email, address=address, contact=contact, pin=pin, user=user)
            cust.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "commonregister.html", {"msg": msg})
######################################################################
#                      COURIER REGISTRATION
######################################################################


def courier(request):
    """ 
        The function to load courier registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]
        try:
            user = User.objects.create_user(
                username=email, password=pwd, is_staff=1, is_active=0)
            user.save()
            cou = Courier.objects.create(
                name=name, email=email, address=address, contact=contact, user=user)
            cou.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "courier.html", {"msg": msg})
######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################


def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "adminhome.html")
######################################################################
#                           CATEGORY
######################################################################


def admincategory(request):
    """ 
        The function to load category page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        cat = request.POST["txtCategory"]

        if Category.objects.filter(category=cat).exists():
            msg = "Data already exist"
        else:
            try:
                db = Category.objects.create(category=cat, status='Active')
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadcategory
    return render(request, "admincategory.html", {"msg": msg, "data": data})


def loadcategory():
    """ 
        The function to load category
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = Category.objects.all()
    return data
######################################################################
#                           BRAND
######################################################################


def adminbrand(request):
    """ 
        The function to load brand page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        cat = request.POST["txtCategory"]

        if Brand.objects.filter(brand=cat).exists():
            msg = "Data already exist"
        else:
            try:

                db = Brand.objects.create(brand=cat, status='Active')
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadbrand
    return render(request, "adminbrand.html", {"msg": msg, "data": data})


def loadbrand():
    """ 
        The function to load brand 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = Brand.objects.all()
    return data
######################################################################
#                           DELETE BRAND
######################################################################


def adminbranddelete(request):
    """ 
        The function to delete brand
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    bid = request.GET.get("id")
    db = Brand.objects.get(id=bid)
    db.delete()
    return HttpResponseRedirect("/adminbrand")
######################################################################
#                           ADMIN COURIER
######################################################################


def admincourier(request):
    """ 
        The function to load courier details
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = Courier.objects.all()
    return render(request, "admincourier.html", {"data": data})
######################################################################
#                           ADMIN UPDATE USER
######################################################################


def adminupdateuser(request):
    """ 
        The function to update user
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    id = request.GET.get("id")
    status = request.GET.get("status")
    data = User.objects.get(id=id)
    if status == 'Approve':
        data.is_active = 1
        data.save()
    else:
        data.delete()
    return HttpResponseRedirect("/admincourier")
######################################################################
#                           RAM
######################################################################


def adminram(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        ram = request.POST["txtRam"]
        size = request.POST["txtSize"]
        speed = request.POST["txtSpeed"]
        bid = request.POST["brand"]
        category = request.POST["category"]
        img = request.FILES["img"]
        rate = request.POST["txtRate"]

        if Ram.objects.filter(name=ram, size=size, speed=speed).exists():
            msg = "Data already exist"
        else:

            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Ram.objects.create(
                    name=ram, size=size, speed=speed, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadram()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminram.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadram():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Ram.objects.all()
    return data
######################################################################
#                           DISPLAY
######################################################################


def admindisplay(request):
    """ 
        The function to load display page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        ram = request.POST["txtRam"]
        size = request.POST["txtSize"]
        speed = request.POST["txtSpeed"]
        panel = request.POST["txtPanel"]
        category = request.POST["txtSpeciality"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]

        if Display.objects.filter(name=ram, size=size, panel=panel).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Display.objects.create(
                    name=ram, size=size, resolution=speed, panel=panel, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loaddisplay()

    brand = loadbrand()
    categ = loadcategory()
    return render(request, "admindisplay.html", {"msg": msg, "data": data, "brand": brand, "categ": categ})


def loaddisplay():
    """ 
    The function to load display 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """
    data = Display.objects.all()
    return data
######################################################################
#                           HDD
######################################################################


def adminhdd(request):
    """ 
        The function to load hdd page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        ram = request.POST["txtRam"]
        size = request.POST["txtSize"]
        speed = request.POST["txtSpeed"]
        bid = request.POST["brand"]
        category = request.POST["category"]
        img = request.FILES["img"]
        rate = request.POST["txtRate"]

        if Hdd.objects.filter(name=ram, speed=speed).exists():
            msg = "Data already exist"
        else:

            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Hdd.objects.create(
                    name=ram, speed=speed, capacity=size, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadhdd()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminhdd.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadhdd():
    """ 
    The function to load hdd 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Hdd.objects.all()
    return data
######################################################################
#                           PROCESSOR
######################################################################


def adminprocessor(request):
    """ 
        The function to load processor page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        ram = request.POST["txtRam"]
        size = request.POST["txtSize"]
        speed = request.POST["txtSpeed"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]

        if Processor.objects.filter(name=ram, cache=size, speed=speed).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Processor.objects.create(
                    name=ram, cache=size, speed=speed, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadprocessor()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminprocessor.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadprocessor():
    """ 
    The function to load processor 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """
    data = Processor.objects.all()
    return data
######################################################################
#                           keyboard
######################################################################


def adminkeyboard(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        type = request.POST["txtType"]
        model = request.POST["txtModel"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]

        if Keyboard.objects.filter(name=name, type=type, model=model).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Keyboard.objects.create(
                    name=name, type=type, model=model, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadkeyboard()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminkeyboard.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadkeyboard():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Keyboard.objects.all()
    return data
######################################################################
#                           Mouse
######################################################################


def adminmouse(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        type = request.POST["txtType"]
        model = request.POST["txtModel"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]
        if Mouse.objects.filter(name=name, type=type).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Mouse.objects.create(
                    name=name, type=type, model=model, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadmouse()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminmouse.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadmouse():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Mouse.objects.all()
    return data
######################################################################
#                           SMPS
######################################################################


def adminsmps(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        type = request.POST["txtType"]
        wattage = request.POST["txtWattage"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]
        if Smps.objects.filter(name=name, type=type).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Smps.objects.create(
                    name=name, type=type, wattage=wattage, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadsmps()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminsmps.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadsmps():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """
    data = Smps.objects.all()
    return data
######################################################################
#                           Motherboard
######################################################################


def adminmotherboard(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        socket = request.POST["txtSocket"]
        type = request.POST["txtType"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES['img']
        if Motherboard.objects.filter(name=name, socket=socket).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Motherboard.objects.create(
                    name=name, socket=socket, chipset=type, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadmotherboard()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "adminmotherboard.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadmotherboard():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Motherboard.objects.all()
    return data
######################################################################
#                           Cables
######################################################################


def admincables(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        type = request.POST["txtType"]
        desce = request.POST["txtDesc"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES['img']
        if Cables.objects.filter(name=name, type=type, desc=desce).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Cables.objects.create(
                    name=name, type=type, desc=desce, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadcables()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "admincables.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadcables():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """
    data = Cables.objects.all()
    return data
######################################################################
#                           Cabin
######################################################################


def admincabinet(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        type = request.POST["txtType"]
        desce = request.POST["txtDesc"]
        material = request.POST["txtMaterial"]
        category = request.POST["category"]
        bid = request.POST["brand"]
        rate = request.POST["txtRate"]
        img = request.FILES["img"]

        if Cabin.objects.filter(name=name, type=type, desc=desce).exists():
            msg = "Data already exist"
        else:
            try:
                brn = Brand.objects.get(id=bid)
                cat = Category.objects.get(id=category)
                db = Cabin.objects.create(
                    name=name, type=type, desc=desce, material=material, category=cat, brand=brn, rate=rate, image=img)
                db.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data added successfully"
    data = loadcabinet()
    datacat = loadcategory()
    brand = Brand.objects.all()
    return render(request, "admincabinet.html", {"msg": msg, "data": data, "brand": brand, "datacat": datacat})


def loadcabinet():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
            tml page
    """

    data = Cabin.objects.all()
    return data
######################################################################
#                      ORDER
######################################################################


def adminorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Assemble.objects.filter(Q(status='Ordered') | Q(
        status='Passed to Courier') | Q(status='Delivered'))
    return render(request, "adminorder.html", {"data": data})
######################################################################
#                      SELECT COURIER
######################################################################


def adminselectcourier(request):
    """ 
        The function to select courier
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    id = request.GET.get("id")
    request.session["oid"] = id

    data = Courier.objects.filter(user__is_active=1)
    return render(request, "adminselectcourier.html", {"data": data})
######################################################################
#                      UPDATE ORDER
######################################################################


def adminupdateorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        oid = request.session["oid"]
        id = request.GET['id']
        db = Assemble.objects.get(id=oid)
        cou = Courier.objects.get(id=id)
        db.status = "Passed to Courier"
        db.save()
        asi = Assign.objects.create(assemble=db, courier=cou)
        asi.save()
        return HttpResponseRedirect("/adminorder")
######################################################################
#                                                                    #
#                                                                    #
#                           COURIER                                #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                      COURIER HOME
######################################################################


def courierhome(request):
    """ 
        The function to load courier home page
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    uid = request.session["uid"]
    data = Courier.objects.get(id=uid)
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        email = request.POST["txtEmail"]
        try:
            data.name = name
            data.address = address
            data.contact = contact
            data.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Updation successfull"

    return render(request, "courierhome.html", {"msg": msg, "d": data})
######################################################################
#                      ORDER
######################################################################


def courierorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    uid = request.session["uid"]

    data = Assign.objects.filter(courier__id=uid)
    return render(request, "courierorder.html", {"data": data})
######################################################################
#                      ORDER
######################################################################


def courierupdate(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    id = request.session["oid"]
    if(request.POST):
        status = request.POST["status"]
        db = Assemble.objects.get(id=id)
        db.status = status
        db.save()
        return HttpResponseRedirect("/courierorder")
    return render(request, "courierupdate.html")
######################################################################
#                                                                    #
#                                                                    #
#                           CCUSTOMER                                #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                      CUSTOMER HOME
######################################################################


def customerhome(request):
    """ 
        The function to load vustomer home page
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    email = request.session["email"]
    uid = request.session["uid"]
    data = Customer.objects.get(id=uid)
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        pin = request.POST["txtPin"]
        email = request.POST["txtEmail"]
        try:
            data.name = name
            data.address = address
            data.contact = contact
            data.pin = pin
            data.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Updation successfull"

    return render(request, "customerhome.html", {"msg": msg, "d": data})
######################################################################
#                      CUSTOMER REQUIREMENT
######################################################################


def customerreq(request):
    """ 
        The function to load customer requirement
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.POST):
        req = request.POST["txtSpeciality"]
        request.session["req"] = req
        return HttpResponseRedirect("/customerdisplay")
    cats = Category.objects.all()
    return render(request, "customerreq.html", {"cats": cats})
######################################################################
#                      CUSTOMER DISPLAY
######################################################################


def customerdisplay(request):
    """ 
    The function to load customer display
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    req = request.session["req"]

    data = Display.objects.filter(category__id=req)
    return render(request, "customerdisplay.html", {"data": data})
######################################################################
#                      CUSTOMER HDD
######################################################################


def customerhdd(request):
    """ 
    The function to load customer hdd
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    display = request.GET.get("id")
    request.session["display"] = display
    req = request.session["req"]

    data = Hdd.objects.filter(category__id=req)
    return render(request, "customerhdd.html", {"data": data})
######################################################################
#                      CUSTOMER RAM
######################################################################


def customerram(request):
    """ 
    The function to load customer ram
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    hdd = request.GET.get("id")
    request.session["hdd"] = hdd
    req = request.session["req"]

    data = Ram.objects.filter(category__id=req)
    return render(request, "customerram.html", {"data": data})
######################################################################
#                      CUSTOMER PROCESSOR
######################################################################


def customerprocessor(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    ram = request.GET.get("id")
    request.session["ram"] = ram
    req = request.session["req"]

    data = Processor.objects.filter(category__id=req)
    return render(request, "customerprocessor.html", {"data": data})
######################################################################
#                      CUSTOMER MOTHERBOARD
######################################################################


def customermotherboard(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    processor = request.GET.get("id")
    request.session["processor"] = processor
    req = request.session["req"]

    data = Motherboard.objects.filter(category__id=req)
    return render(request, "customermotherboard.html", {"data": data})
######################################################################
#                      CUSTOMER SMPS
######################################################################


def customersmps(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    motherboard = request.GET.get("id")
    request.session["motherboard"] = motherboard
    req = request.session["req"]

    data = Smps.objects.filter(category__id=req)
    return render(request, "customersmps.html", {"data": data})
######################################################################
#                      CUSTOMER CABLES
######################################################################


def customercables(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    smps = request.GET.get("id")
    request.session["smps"] = smps
    req = request.session["req"]

    data = Cables.objects.filter(category__id=req)
    return render(request, "customercables.html", {"data": data})
######################################################################
#                      CUSTOMER CABINET
######################################################################


def customercabinet(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    cables = request.GET.get("id")
    request.session["cables"] = cables
    req = request.session["req"]

    data = Cabin.objects.filter(category__id=req)
    return render(request, "customercabinet.html", {"data": data})
######################################################################
#                      CUSTOMER KEYBOARD
######################################################################


def customerkeyboard(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    cabinet = request.GET.get("id")
    request.session["cabinet"] = cabinet
    req = request.session["req"]

    data = Keyboard.objects.filter(category__id=req)
    return render(request, "customerkeyboard.html", {"data": data})
######################################################################
#                      CUSTOMER MOUSE
######################################################################


def customermouse(request):
    """ 
    The function to load customer processor
    -----------------------------------------------
    Parameters: 
        HTTP request 

    Returns: 
        html page
    """

    keyboard = request.GET.get("id")
    request.session["keyboard"] = keyboard
    req = request.session["req"]

    data = Mouse.objects.filter(category__id=req)
    return render(request, "customermouse.html", {"data": data})
######################################################################
#                      CUSTOMER SELECT PROCESSOR
######################################################################


def customerslctpro(request):
    """ 
        The function to load selected items
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
    """
    if(request.GET):
        req = request.session["req"]
        email = request.session["email"]
        uid = request.session["uid"]

        mouse = request.GET["id"]
        mouseData = Mouse.objects.get(id=mouse)
        mourate = mouseData.rate

        keyboard = request.session["keyboard"]
        keyData = Keyboard.objects.get(id=keyboard)
        keyrate = keyData.rate

        motherboard = request.session["motherboard"]
        mothData = Motherboard.objects.get(id=motherboard)
        morate = mothData.rate

        cables = request.session["cables"]
        cableData = Cables.objects.get(id=cables)
        cabrate = cableData.rate

        smps = request.session["smps"]
        smpsData = Smps.objects.get(id=smps)
        smpsrate = smpsData.rate

        cabinet = request.session["cabinet"]
        cabData = Cabin.objects.get(id=cabinet)
        cnetrate = cabData.rate

        processor = request.session["processor"]
        proData = Processor.objects.get(id=processor)
        prorate = proData.rate

        display = request.session["display"]
        disData = Display.objects.get(id=display)
        disrate = disData.rate

        hdd = request.session["hdd"]
        hddData = Hdd.objects.get(id=hdd)
        hddrate = hddData.rate

        ram = request.session["ram"]
        ramData = Ram.objects.get(id=ram)
        ramrate = ramData.rate

        total = int(prorate)+int(disrate)+int(hddrate)+int(ramrate) + \
            int(keyrate)+int(morate)+int(mourate) + \
            int(cabrate)+int(cnetrate)+int(smpsrate)

        cust = Customer.objects.get(id=uid)
        cat = Category.objects.get(id=req)
        db = Assemble.objects.create(customer=cust, request=cat, display=disData, cabin=cabData, cables=cableData, hdd=hddData, keyboard=keyData,
                                     motherboard=mothData, mouse=mouseData, processor=proData, ram=ramData, smps=smpsData, total=total, status='Ordered')
        db.save()
        return HttpResponseRedirect(f"/customerassemble?id={db.id}")
######################################################################
#                      CUSTOMER ASSEMBLE
######################################################################


def customerassemble(request):
    """ 
        The function to load selected items
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    asId = request.GET['id']

    data = Assemble.objects.get(id=asId)
    if 'pay' in request.POST:
        return HttpResponseRedirect("/payment")
    if 'cart' in request.POST:
        data.status = 'In Cart'
        data.save()
        return HttpResponseRedirect("/customercart")
    return render(request, "customerassemble.html", {"d": data})

######################################################################
#                      CUSTOMER CART
######################################################################


def customercart(request):
    """ 
        The function to load cart
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    uid = request.session["uid"]

    data = Assemble.objects.filter(customer__id=uid, status='In Cart')
    amt = 0
    for d in data:
        amt += int(d.total)
    if 'pay' in request.POST:
        for d in data:
            d.status = 'Ordered'
            d.save()
        return HttpResponseRedirect(f"/payment?amt={amt}")
    return render(request, "customercart.html", {"data": data, "amt": amt})


######################################################################
#                      PAYMENT
######################################################################


def payment(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    amt = request.GET['amt']

    if(request.POST):

        return HttpResponseRedirect("/customerassembleorder")
    return render(request, "payment.html", {"amt": amt})
######################################################################
#                      PIN
######################################################################


def pin(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    ppin = request.session['ppin']
    ppin = request.GET.get("i")
    if(request.POST):
        pin = request.POST["pin"]

        if(pin == ppin):
            return HttpResponseRedirect("/customerassembleorder")
    return render(request, "pin.html")
######################################################################
#                      ASSEMBLED ORDER
######################################################################


def customerassembleorder(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = Assemble.objects.filter(Q(customer__id=uid) &
                                   (Q(status='Ordered') | Q(status='Passed to Courier') | Q(status='Delivered')))
    return render(request, "customerassembleorder.html", {"data": data})
