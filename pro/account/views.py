from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import RegForm
from django.contrib import messages

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
            return redirect("h")
        else:
            messages.error(request,"user registration failed !!")
            return render(request,"reg.html",{"form":form_data})

       

