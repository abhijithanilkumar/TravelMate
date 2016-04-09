from django.shortcuts import render
from models import *

# Create your views here.

def searchbusPage(request):
    if request.method == 'GET':
        return render(request,'searchbus.html')
    if request.method == 'POST':
        return render(request,'searchbus.html')

def searchcarPage(request):
    return render(request,'searchcar.html')
