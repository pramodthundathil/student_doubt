from turtle import mode
from django.db import models
from django.contrib.auth.models import User

import doubts

# Create your models here.

class Student_Doubts(models.Model):
    
    QuestionID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Student_Name = models.CharField(max_length=100,null=True)
    TeacherID = models.CharField(max_length=100,null=True)
    Teacher_Name = models.CharField(max_length=100,null=True)
    Question = models.CharField(max_length=1000)
    Question_date = models.DateTimeField(auto_now_add=False,null=True)
    Answer = models.CharField(max_length=1000,null=True)
    answer_date = models.DateTimeField(auto_now_add=False,null=True)
    category  = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    
