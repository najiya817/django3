from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import RegisterForm,LoginForm

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"main_home.html")

class RegView(View):
        def get(self,request,*args,**kwargs):
            f=RegisterForm()
            return render(request,"reg.html",{"data":f})
        def post(self,request,*args,**kwargs):
            return HttpResponse("yeah")
             

class LogView(View):
        def get(self,request,*args,**kwargs):
            f=LoginForm()
            return render(request,"log.html",{"data:f"})
        def post(self,request,*args,**kwargs):
            return HttpResponse("hoo")

