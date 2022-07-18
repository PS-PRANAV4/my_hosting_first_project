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


def report(request):
    # aalbin = marks.objects.filter(mark_for = "aalbin").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # anandhu = marks.objects.filter(mark_for = "anandhu").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # danish = marks.objects.filter(mark_for = "danish").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # deepthi = marks.objects.filter(mark_for = "deepthi").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # sai = marks.objects.filter(mark_for = "sai").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # shahidha = marks.objects.filter(mark_for = "shahidha").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # vyshnav = marks.objects.filter(mark_for = "vyshnav").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # nabeel = marks.objects.filter(mark_for = "nabeel").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # arun = marks.objects.filter(mark_for = "arun").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )

    # pranav = marks.objects.filter(mark_for = "pranav").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # sidharth = marks.objects.filter(mark_for = "sidharth").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
    # abin = marks.objects.filter(mark_for = "abin").aggregate(  confi = Sum('confidence'), content = Sum('content'), fluency = Sum('fluency'),count = Count('mark_for') )
   
    # context = {'aalbin': aalbin,'anandhu':anandhu,'danish':danish,'deepthi':deepthi,'sai':sai,'shahidha':shahidha,'vyshnav':vyshnav,'nabeel':nabeel,
    # 'arun':arun,'pranav':pranav,'sidharth':sidharth,'abin':abin,
    
    # }

    markss = marks.objects.values('mark_for').annotate(confi = Avg('confidence',distinct=True),content = Avg('content',distinct=True),fluency = Avg('fluency',distinct=True))


    print(report)
    return render(request,'give.html',{"marks":markss}) 

def delet(request):
    try:
        reports = marks.objects.all()
        reports.delete()
    except:
        pass
    return redirect(report)
