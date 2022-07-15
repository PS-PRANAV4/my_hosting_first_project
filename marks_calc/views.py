from itertools import count
from unicodedata import name
from django.shortcuts import redirect, render
from .models import author,marks
import json
from django.http import HttpResponse, JsonResponse
from django.db.models import Count,Avg,Sum

# Create your views here.


def authors(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        my = author.objects.create(auther_name = name)
        return redirect(mark,my.id)
    return render(request,'mark.html')

def mark(request,id):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body['username']
        confidence = body['confidence']
        content = body['content']
        fluency =  body['fluency']
        auth = author.objects.get(id = id)
        print(confidence,username,content,fluency)
        marks.objects.create(mark_for = username,confidence = confidence, content = content, fluency = fluency,auther = auth )
        data = {'user': username}
        return JsonResponse(data)



    return render(request,'enter.html',{'id':id})


def report(request,name):
    report = marks.objects.filter(mark_for = name).aggregate(  confi = Sum('confidence'), conntent = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    print(report)
    print(f"confi = {report['confi']/report['count']} conte = {report['conntent']/report['count']} flue = {report['fluency']/report['count']}") 
    return HttpResponse(request,'report')