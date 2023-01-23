from django.urls import path
from .views import AddMark,AddStudentView

urlpatterns=[
    path('addmrk/',AddMark.as_view(),name="markk"),
    path('addstu/',AddStudentView.as_view(),name="addstudent")

]