from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.forms import TOPIC as TOPICForm, WEBPAGE as WEBPAGEForm

def insert_topic(request):
    ETFO = TOPICForm()
    d = {'ETFO': ETFO}

    if request.method == 'POST':
        TFDO = TOPICForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'insert_topic.html', d)

def insert_webpage(request):
    EWFO = WEBPAGEForm()
    d = {'EWFO': EWFO}

    if request.method == 'POST':
        WFDO = WEBPAGEForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'insert_webpage.html', d)
