from django.shortcuts import render

# Create your views here.

def home(request):
    d={'age':28}
    return render(request,'home1.html',context=d)