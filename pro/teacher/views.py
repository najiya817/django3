from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import AddMarkForm,StudentForm
from django.contrib import messages
from .models import StudentModel

# Create your views here.
class AddMark(View):
    def get(self,request,*args,**kwargs):
        f=AddMarkForm()
        return render(request,"addmark.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=AddMarkForm(data=request.POST)
        if form_data.is_valid():
            num1=form_data.cleaned_data.get("mark1")
            num2=form_data.cleaned_data.get("mark2")
            num3=form_data.cleaned_data.get("mark3")
            num4=form_data.cleaned_data.get("mark4")
            num5=form_data.cleaned_data.get("mark5")
            res=int(num1)+int(num2)+int(num3)+int(num4)+int(num5)
            return render(request,"addmark.html",{"data":res})
        else:
            return render(request,"addmark.html",{"form":form_data})
    
class AddStudentView(View):
    def get(self,request,*args,**kwargs):
        f=StudentForm()
        return render(request,"addstu.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=StudentForm(data=request.POST)
        if form_data.is_valid():
           fn=form_data.cleaned_data.get("first")
           ln=form_data.cleaned_data.get("last")
           ag=form_data.cleaned_data.get("age")
           ph=form_data.cleaned_data.get("phone")
           email=form_data.cleaned_data.get("email")
           addr=form_data.cleaned_data.get("address")
           StudentModel.objects.create(first=fn,last=ln,age=ag,phone=ph,email=email,address=addr)
           messages.success(request,"student added succesfull")
           return redirect("h")
        else:
            messages.error(request,"student adding failed!!")
            return render(request,"addstu.html",{"form":form_data})
        

class StudentListView(View):
    def get(self,request,*args,**kwargs):
        res=StudentModel.objects.all()
        return render(request,"viewstudent.html",{"data":res})

class StudDeleteView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("id")
        stu=StudentModel.objects.get(id=sid)
        stu.delete()
        return redirect("viewstu")