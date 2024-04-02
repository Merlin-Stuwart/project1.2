from django.shortcuts import render

# Create your views here.

def home(request):
    d={'menu':'Dishes'}
    return render(request,'home.html',context=d)