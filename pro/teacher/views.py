from django.shortcuts import render
from django.views.generic import View
from .forms import AddMarkForm

# Create your views here.
class AddMark(View):
    def get(self,request,*args,**kwargs):
        f=AddMarkForm()
        return render(request,"addmark.html",{"form":f})
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("mark1")
        num2=request.POST.get("mark2")
        num3=request.POST.get("mark3")
        num4=request.POST.get("mark4")
        num5=request.POST.get("mark5")
        res=int(num1)+int(num2)+int(num3)+int(num4)+int(num5)
        return render(request,"addmark.html",{"data":res})
