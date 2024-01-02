from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import  messages,auth


from .forms import  Register
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('school_app:detail_user')
            #return redirect('/')
        else:
            messages.info(request,"invalid...try again")
            return redirect('school_app:login_user')
           # return redirect('/')
    return render(request,'login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['confpassword']

        if(password  == con_password ):
            if User.objects.filter(username=username).exists():
                messages.info(request,"The username is already taken try another one.....")
                return redirect('school_app:register_user')
            else:
                user_1 = User.objects.create_user(username=username,password=password)
                user_1.save()
                messages.info(request,"Done....")
                return redirect('school_app:login_user')
                #return redirect('/')
        else:
            messages.info(request,"The password doesnot match..try agin")
            return redirect('school_app:register_user')
            #return redirect('/')

    return render(request,'register.html')

def detail_user(request):
    # Implement registration logic
    if request.method == 'POST':
        username = request.POST['username']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        email =  request.POST['email']
        address = request.POST['address']
        purpose = request.POST['Purpose']
        dept = request.POST.get('dept','')
        course = request.POST.get('course','')
        materials = request.POST.get('materials_provided','')

        if not username or not dob or not age or not gender or not email or not address or not purpose or not dept or not course or not materials:
            messages.error(request, "All fields must be filled in.")
            return redirect('school_app:detail_user')
        else:
            messages.info(request,"Order Placed")





    return render(request, 'detail.html')