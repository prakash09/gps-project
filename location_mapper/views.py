from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def get_location(request): 
    return render(request,'index.html')
def get_vehicle(request):
    device_id=request.GET['device_id']
    return HttpResponse(json.dumps({'device_id':device_id,'lat':25,'lon':75}))
