from django.urls import path
from.import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.signin,name='signin'),
    path('signin',views.signin,name='signin2'),
    path('registration',views.registration,name='registration'),
    
    path('teacher_view',views.teacher_view,name='teacher_view'),
    path('student_view',views.student_view,name='student_view'),
    
    path('signout',views.signout,name='signout'),
    path('teacher',views.teacher,name='teacher'),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("StudentsDoubts",views.StudentsDoubts,name="StudentsDoubts")
] 