from django.shortcuts import render
from app.models import *

# Create your views here.
def book(request):
    QLBO=Book.objects.all()
    d={'QLBO':QLBO}
    return render(request,"book.html",context=d)


def author(request):
    QLAO=Author.objects.all()
    d={'QLAO':QLAO}
    return render(request,'Author.html',d)
