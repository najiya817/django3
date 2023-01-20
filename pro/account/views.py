from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"main_home.html")

class RegView(View):
        def get(self,request,*args,**kwargs):
            return render(request,"reg.html")

class LogView(View):
        def get(self,request,*args,**kwargs):
            return render(request,"log.html")
