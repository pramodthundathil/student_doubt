from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .decorators import unautenticated_user,allowed_users, admin_only

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import Group

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from .forms import UserRegistration
from doubts.models import Student_Doubts

# Create your views here.
@login_required(login_url='signin')  
@admin_only
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render (request,'index.html')

@login_required(login_url='signin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def student_view(request):
    Q_and_A = Student_Doubts.objects.all().order_by('-QuestionID')
    
    return render (request,'index.html',{"QA":Q_and_A})

@login_required(login_url='signin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def teacher_view(request):
    
    # if request.method == 'POST':
        
    #     questionID = request.POST['submit']
    #     Q_and_A = Student_Doubts.objects.filter(QuestionID = questionID )
    #     return render(request,'doubts_answer.html',{'items':Q_and_A})
        
    Q_and_A = Student_Doubts.objects.all()
    return render (request,'teacher_home.html',{"QA":Q_and_A})


def StudentsDoubts(request):
    Q_and_A = Student_Doubts.objects.all()
    return render(request,"studentdoubtteacher.html",{"QA":Q_and_A})

def AdminIndex(request):
    users = User.objects.all()
    form = UserRegistration()
    
    if request.method == 'POST':
        
        form = UserRegistration(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('AdminIndex')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('AdminIndex')
            
            else:
                user = form.save()
                user.save()
                
                group = Group.objects.get(name='teacher')
                user.groups.add(group)       
                
                username = form.cleaned_data.get('username')
                messages.info(request,"Account Was Created")
                return redirect('AdminIndex')
    
    return render(request,"adminindex.html",{"form":form,"users":users})
    

@unautenticated_user
def signin(request):
    
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user)
            return redirect('index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('signin')
    
    return render(request,'login.html')

@unautenticated_user
def registration(request):
    
    form = UserRegistration()
    
    if request.method == 'POST':
        
        form = UserRegistration(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                user = form.save()
                user.save()
                
                group = Group.objects.get(name='student')
                user.groups.add(group)       
                
                username = form.cleaned_data.get('username')
                messages.info(request,"Account Was Created")
                return redirect('signin')
    
    return render(request,'register.html',{"form":form})

def signout(request):
    logout(request)
    return redirect('signin')

def teacher(request):
    users = User.objects.all()
    return render (request,'teacher.html',{"users":users})