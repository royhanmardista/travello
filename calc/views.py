from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) : 
    return render(request, 'home.html', {'name' : 'navin'})

def add(request) :
    result = int(request.POST['number1']) + int(request.POST['number2']) + int(request.POST['number3'])
    return render(request, 'add.html' , {'result' : result})
