from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect,HttpResponse
from .models import Languages_offered,Contact_us,Langs,Teachers,user_Registration,tutor_Registration,SC
from django.contrib import messages

def home(request):
    lo = Languages_offered.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact_us(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'index.html', {'result': lo})
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact_us(name=name, email=email, phone=phone, message=message)
        contact.save()
        return redirect("/")
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def loginasuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'afterlogin.html')
    return render(request,'loginasuser.html')

def loginastutor(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        tut = tutor_Registration.objects.filter(username=username).values()
        status = tut[0]['interview']
        if status:
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'teacherlogin.html')
        else:
            return HttpResponse("Logging in could be possible after you get selected through a telephonic interview, which you could expect within two days")
    return render(request,'loginastutor.html')

def signupasuser(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        user= User.objects.create_user(first_name=first_name,username=username,password=password)
        user.save()
       
        login(request,user)
        return redirect('/userpage')
    return render(request,'signupasuser.html')
def signupastutor(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        user= User.objects.create_user(first_name=first_name,username=username,password=password)
        user.save()
        login(request,user)
        return redirect('/userpage1')
    return render(request,'signupastutor.html')
#@login_required(login_url='/teacherlogin')
def userpage(request):
        if request.method == 'POST':
            username = request.user.username
            name= request.POST.get('name')
            lang= request.POST.get('lang')
            email= request.POST.get('email')
            phone= request.POST.get('phone')
            password= request.POST.get('password')
            password1= request.POST.get('password1')
            if password==password1:
                registration = user_Registration(username=username,name=name, lang=lang, email=email, phone=phone,password=password)
                registration.save();
                print("User Created")
                return redirect('/')
            else:
                print("Passsword Not matching, Try again")
        return render(request,'userpage.html')

@login_required(login_url='/signupastutor')
def userpage1(request):
        if request.method == 'POST':
            username = request.user.username
            name= request.POST.get('name')
            lang= request.POST.get('lang')
            email= request.POST.get('email')
            phone= request.POST.get('phone')
            password= request.POST.get('password')
            password1= request.POST.get('password1')
            if password==password1:
                registration = tutor_Registration(username=username,name=name, lang=lang, email=email, phone=phone,password=password)
                registration.save()
                print("User Created")
                return redirect('/')
            else:
                print("Passsword Not matching, Try again")
        return render(request,'userpage1.html')

def afterlogin(request):
    return render(request,'afterlogin.html')

def languages(request):
    langs = Langs.objects.all()
    return render(request,'languages.html',{'res':langs})

def choiceofteacher(request):
    teacher=Teachers.objects.all()
    user =  request.user.username
    teacher = tutor_Registration.objects.filter(name=user).values()
    return render(request,'choiceofteacher.html',{'res1':teacher})

def profilepage(request):
    return render(request,'profilepage.html')

def teacherlogin(request):
    return render(request,'teacherlogin.html')
@login_required(login_url='/signupastutor')

def teacherprofile(request):
    user =  request.user.username
    stud = Teachers.objects.filter(username=user).values()
    return render(request,'teacherprofile.html',{'res2':stud})

def scheduleclass(request):
    if request.method == 'POST':
        day= request.POST.get('day')
        time= request.POST.get('time')
        note= request.POST.get('note')
        sclass=SC(day=day,time=time,note=note)
        sclass.save();
        return redirect('/teacherstudent')
    return render(request,'scheduleclass.html')

def teachers(request):
    teacher=Teachers.objects.all()
    # user =  request.user.username
    # teacher=tutor_Registration.objects.filter(lang=user).values()
    return render(request,'teachers.html',{'res1':teacher})

def teacherstudent(request):
    user =  request.user.username
    stud = user_Registration.objects.all()
    return render(request,'teacherstudent.html',{'res3':stud})

@login_required(login_url='/signupasuser')

def studentprofile(request):
    user =  request.user.username
    stud = user_Registration.objects.filter(username=user).values()
    return render(request,'studentprofile.html',{'res2':stud})

def joincall(request):
    return render(request,'joincall.html')

def call(request):
    return render(request,'call.html')

def payment(request):
    return render(request,'payment.html')

def logout(request):
    return render(request,'logout.html')
