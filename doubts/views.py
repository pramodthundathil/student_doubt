from ast import Global
from django.shortcuts import redirect, render
from .models import Student_Doubts
from django.contrib.auth.models import User
from datetime import datetime

from django.contrib import messages

# Create your views here.

def ask_doubts(request):
    
    if request.method == 'POST':
        
        username = request.session['username']
        user = User.objects.get(username = username)
        
        Student_name = request.POST['student_name']
        Question = request.POST['student_doubts']
        cat = request.POST['cat']
        StudentID = user.id
        
        question = Student_Doubts.objects.create(StudentID = request.user,Student_Name =Student_name,Question = Question,Question_date = datetime.now(),category = cat,subject = cat)
        question.save()
        messages.info(request,'Question Submited for Verification')
        return redirect('index')
    
    return render(request,'doubts_ask.html')

def answer_douts(request):
    
    questionID = request.POST['submit']
    Q_and_A = Student_Doubts.objects.filter(QuestionID = questionID )        
    
    return render(request,'doubts_answer.html',{'items':Q_and_A})

def answer_it(request,pk):
    if request.method == 'POST':
        Q_and_A = Student_Doubts.objects.get(QuestionID = pk )     
        Q_and_A.Teacher_Name  = request.user.first_name
        Q_and_A.Answer  = request.POST['answer']
        Q_and_A.TeacherID = request.user.id
        Q_and_A.answer_date = datetime.now()
        Q_and_A.save()
         
        messages.info(request,'Answer submitted')
        return redirect('StudentsDoubts')
    return redirect('StudentsDoubts')
    
     
def DoubtsStudent(request):
    doubts = Student_Doubts.objects.filter(StudentID = request.user)
    return render(request,"deletestudent.html",{"doubts":doubts})

def deletedoubts(request,pk):
    Student_Doubts.objects.get(QuestionID = pk).delete()
    messages.info(request,'item delated')
    return redirect("DoubtsStudent")

def Myanswers(request):
    doubts = Student_Doubts.objects.filter(TeacherID = request.user.id)
    
    return render(request,'myanswers.html',{"doubts":doubts})

def updateanswer(request,pk):
    if request.method =="POST":
        douts = Student_Doubts.objects.get(QuestionID = pk)
        ans = request.POST['answer']
        douts.Answer = ans
        douts.answer_date = datetime.now()
        douts.save()
        messages.info(request,"Data Updated")
        return redirect("Myanswers")
    
def deleteteacherdoubt(request,pk):
    douts = Student_Doubts.objects.get(QuestionID = pk)
    douts.delete()
    messages.info(request,"Item deleted")
    return redirect("Myanswers")
