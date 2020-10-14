from django.shortcuts import render
from django.http import HttpResponse
from .models import presentation
from .models import journals
from .models import conference
from .models import Video

# Create your views here.

#for home page 
def home(request):
    return render(request,"index.html",{'title':'Home'})



#for publication page journal confarence page 
def publicatin(request):
    journalsdata=journals.objects.all()
    confarencedata=conference.objects.all()
    return render(request, "publication.html",{'title':'Publication','paper':journalsdata,'confarence': confarencedata})


def contact(request):
    return render(request, "contact.html",{'title':'Contact'})


def presentationaward(request):
    presentationdata = presentation.objects.all()
    return render(request, "presntation.html",{'title':'Presentation','present': presentationdata})

def research(request):
    return render(request, "research.html",{'title':'Research' })

def teaching(request):
    video=Video.objects.all()
    return render(request, "teaching.html",{'title':'Teaching','video':video})




    