from django.shortcuts import render

def home(request):
   return render(request,'home.html')


def information(request):
    return render(request,'information.html',{})

def contact(request):
    return render(request,'contact.html',{})

