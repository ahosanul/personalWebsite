from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"index.html",{'title':'Home'})


def publicatin(request):
    return render(request, "publication.html",{'title':'Publication'})


def contact(request):
    return render(request, "contact.html",{'title':'Contact'})


def presentation(request):
    return render(request, "presntation.html",{'title':'Presentation'})

def research(request):
    return render(request, "research.html",{'title':'Research'})

def teaching(request):
    return render(request, "teaching.html",{'title':'Teaching'})

    