from django.urls import path
from.import views

urlpatterns = [
    
    path('ask_doubts',views.ask_doubts,name='ask_doubts'),
    path('answer_douts',views.answer_douts,name= 'answer_douts'),
    path('answer_it/<int:pk>',views.answer_it,name ='answer_it'),
    path("DoubtsStudent",views.DoubtsStudent,name="DoubtsStudent"),
    path("deletedoubts/<int:pk>",views.deletedoubts,name="deletedoubts"),
    path("Myanswers",views.Myanswers,name="Myanswers"),
    path("updateanswer/<int:pk>",views.updateanswer,name="updateanswer"),
    
    
    
]