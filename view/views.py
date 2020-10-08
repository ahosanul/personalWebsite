from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"index.html",{'title':'Home'})


def publicatin(request):
    return render(request, "publication.html",{'title':'Publication'})