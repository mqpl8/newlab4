from django.shortcuts import render
from django.http import HttpResponse

taxRate=15/100

# Create your views here.

def index(request):
    return render(request, "taxapp/index.html")

def taxadd(request, number):
    num=int(number)
    num=(num*taxRate)+num
    
    return HttpResponse(f"{num}$")

def rate(request):
    return render(request, "taxapp/rate.html",{
        "taxrate":(taxRate)*100
    })

