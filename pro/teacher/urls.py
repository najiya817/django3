from django.urls import path
from .views import *

urlpatterns=[
    path('addmrk/',AddMark.as_view(),name="markk"),
    path('addstu/',AddStudentMView.as_view(),name="addstudent"),
    path('viewstudent/',StudentListView.as_view(),name="viewstu"),
    path('delstudent/<int:id>',StudDeleteView.as_view(),name="delstu"),
    path('editstudent/<int:id>',StudEditMView.as_view(),name="editstu"),

    

]