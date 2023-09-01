from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def Insert_topic(request):
    tn=input('enter topic name : ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('data is inserted to topics')

def Insert_webpage(request):
    tn=input('enter topic name : ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    
    return HttpResponse('data inserted to webpage')

def Insert_accessrecord(request):
    tn=input('enter topic name : ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL: ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter date : ')
    a=input('enter author : ')
    e=input('enter email : ')
    ao=AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    return HttpResponse('data inserted to author')
