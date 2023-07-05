from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def members(request):
    return HttpResponse("<h1>Hello World</h1><br/><a href='https://devmap.ir'>devmap.ir</a>")
def index(request):
    return render(request,'index.html')

    

