from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import cstmrdata

def about(req):
    template=loader.get_template('about.html')
    data={}
    response=template.render(data,req)
    return HttpResponse(response)

def cstmrdata_save(req):
    print(req.POST)
    print(req.POST['name'])
    print(req.POST['place'])
    print(req.POST['email'])
    print(req.POST['phone'])
    print(req.POST['password'])
    customer= cstmrdata(name=req.POST['name'],place=req.POST['place'],
                           email=req.POST['email'],mobile=req.POST['phone'],
                           password=req.POST['password'])
    customer.save()
    return HttpResponse ('Saved data successfully')