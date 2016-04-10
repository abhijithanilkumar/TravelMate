from django.shortcuts import render
from models import *

# Create your views here.

def searchbusPage(request):
    if request.method == 'GET':
        return render(request,'searchbus.html')
    if request.method == 'POST':
        source = request.POST.get('source','')
        destination = request.POST.get('destination','')
        date = request.POST.get('date','')
        time = request.POST.get('time','')
        return render(request,'buslist.html')

def searchcarPage(request):
    if request.method == 'GET':
        return render(request,'searchcar.html')
