from django.shortcuts import render
from django.http import HttpResponse
import json
import random
from location_mapper.models import VehicleLocation

def save_location(request):
    device_id=request.GET['device_id']
    lat=request.GET['lat']
    lon=request.GET['lon']
    VehicleLocation.objects.create(device_id=device_id,lat=lat, lon=lon)
    return HttpResponse("success")

def get_location(request):
    return render(request,'index.html')

def get_vehicle(request):
    device_id=request.GET['device_id']
    try:
        data=VehicleLocation.objects.filter(device_id=device_id).order_by('-id')[:1][0]
    except:
        return HttpResponse("error")
    return HttpResponse(json.dumps({'device_id':data.device_id,'lat':data.lat,'lon':data.lon}))
