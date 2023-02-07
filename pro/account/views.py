from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import LogForm, RegForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        user="Ajith"
        return render(request,"main_home.html",{"user_name":user})

class RegView(View):
    def get(self,request,*args,**kwargs):
        f=RegForm()
        return render(request,"reg.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"user registered succesfull !!")
            return redirect("log")
        else:
            messages.error(request,"user registration failed !!")
            return render(request,"reg.html",{"form":form_data})
        

class LogView(View):
    def get(self,request,*args,**kwargs):
        f=LogForm()
        us=request.user
        return render(request,"log.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("uname")
            ps=form_data.cleaned_data.get("pswd")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                messages.success(request,"login succesfull")
                return redirect("h")
            else:
                messages.error(request,"login failed!!")
                return redirect("log")
        else:
            return render(request,"log.html",{"form":form_data})


       
class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")
