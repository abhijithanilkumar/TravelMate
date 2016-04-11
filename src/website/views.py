from django.shortcuts import render
from models import *

# Create your views here.

def searchbusPage(request):
    if request.method == 'GET':
        return render(request,'searchbus.html')
    if request.method == 'POST':
        btype = []
        source = request.POST.get('source','')
        destination = request.POST.get('destination','')
        routes = Route.objects.filter(stops__name=source).filter(stops__name=destination)
        bus = Bus.objects.filter(route__in=routes)
        for item in bus:
            stop = Stop.objects.filter(name=source)
            srctime = stop.get(route=item.route).time
            stop = Stop.objects.filter(name=destination)
            dsttime = stop.get(route=item.route).time
            btype.append(BusDetail(name=item.name,route=item.route.name,src=source,dst=destination,srct=srctime,dstt=dsttime,contact=item.contact))
        return render(request,'buslist.html',{'bus':btype})

def searchcarPage(request):
    if request.method == 'GET':
        return render(request,'searchcar.html')
    if request.method == 'POST':
        ctype = []
        source = request.POST.get('source','')
        destination = request.POST.get('destination','')
        routes = Route.objects.filter(stops__name=source).filter(stops__name=destination)
        car = Pooling.objects.filter(route__in=routes)
        print car
        for item in car:
            stop = Stop.objects.filter(name=source)
            srctime = stop.get(route=item.route).time
            stop = Stop.objects.filter(name=destination)
            dsttime = stop.get(route=item.route).time
            ctype.append(CarDetail(name=item.user.get_full_name(),route=item.route.name,src=source,dst=destination,srct=srctime,dstt=dsttime,seats=item.seats,contact=item.contact))
        print ctype
        return render(request,'carlist.html',{'car':ctype})
