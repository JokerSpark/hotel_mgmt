from django.shortcuts import render,redirect
from main import forms
from main import models

# Create your views here.
#ADMIN
#---------------------------------------------------------------------------------------------------------------------------------

def main_admin(request):
    return render(request,'main_admin.html')

#ROOMS
#----------------------------------------------------------------------------------------------------------------------------
def room_mgmt(request):
    return render(request,'roommanagement.html')


def add_room(request):
    if request.method == "POST":
        form = forms.room_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_room")
        else:
            return redirect('/add_room')
    else:
        form = forms.room_form()
        context = {'form':form}
        return render(request,'add_room.html',context)


def view_room(request):
    form = models.Room.objects.all()
    context = {"form": form}
    return render(request,'view_room.html',context)


def update_room(request,id):
    data = models.Room.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        form = forms.room_form(request.POST,instance = data)
    
        if form.is_valid():
         
            form.save()
            return redirect("/view_room")
    return render(request,"update_room.html",context) 



def delete_room(request,id):
    data = models.Room.objects.get(id=id)
    data.delete()
    return redirect("/view_room")

#rooms
#-----------------------------------------------------------------------------------------------------------------------




#STAFFS
#---------------------------------------------------------------------------------------------------------------------------
def staff_mgmt(request):
    return render(request,'staff_management.html',)
    

def add_staff(request):
    if request.method == "POST":
        form = forms.staff_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_staff")
        else:
            return redirect('/add_staff')
    else:
        form = forms.staff_form()
        context = {'form':form}
    return render(request,'add_staff.html',context)

def view_staff(request):
    form = models.Staff.objects.all()
    context = {"form": form}
    return render(request,'view_staff.html',context)




def update_staff(request,id):
    data = models.Staff.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        form = forms.staff_form(request.POST,instance = data)
   
        if form.is_valid():

            form.save()
            return redirect("/view_staff")
    return render(request,"update_staff.html",context) 



def delete_staff(request,id):
    data = models.Staff.objects.get(id=id)
    data.delete()
    return redirect("/view_staff")


#staffs
#-----------------------------------------------------------------------------------------------------------------------------


#RESTRARENT
#-----------------------------------------------------------------------------------------------------------------------
def rest_mgmt(request):
    return render(request,'restrarent_management.html')


def add_rest(request):
    if request.method == "POST":
        form = forms.rest_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_rest")
        else:
            return redirect('/add_rest')
    else:
        form = forms.rest_form()
        context = {'form':form}
    return render(request,'add_rest.html',context)



def view_rest(request):
    form = models.Restaurants.objects.all()
    context = {"form": form}
    return render(request,'view_restrarent.html',context)



def update_rest(request,id):
    data = models.Restaurants.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        form = forms.update_rest_form(request.POST,instance = data)

        if form.is_valid():

            form.save()
            return redirect("/view_rest")
    return render(request,"update_rest.html",context)


def delete_rest(request,id):
    data = models.Restaurants.objects.get(id=id)
    data.delete()
    return redirect("/view_rest")


#restrarent
#-------------------------------------------------------------------------------------------------------------------------------




#USER
#----------------------------------------------------------------------------------------------------------------------------


def user_mgmt(request):
    return render(request,'user_management.html')

def add_user(request):
    if request.method == "POST":
        form = forms.Customer_form(request.POST,request.FILES)
        print('step 1')
        if form.is_valid():
            print('step 2')
            form.save()
            print('step 3')
            return redirect("/view_user")
        else:
            return redirect('/add_user')
    else:
        form = forms.Customer_form()
        context = {'form':form}
    return render(request,'add_user.html',context)



def view_user(request):
    form = models.Customer.objects.all()
    context = {"form": form}
    return render(request,'view_user.html',context)



def update_user(request,id):
    data = models.Customer.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        form = forms.update_customer_form(request.POST,request.FILES,instance = data)

        if form.is_valid():

            form.save()
            return redirect("/view_user")
    return render(request,"update_user.html",context)


def delete_user(request,id):
    data = models.Customer.objects.get(id=id)
    data.delete()
    return redirect("/view_user")


#user
#-----------------------------------------------------------------------------------------------------------------------------------

#admin
#------------------------------------------------------------------------------------------------------------------------------
























