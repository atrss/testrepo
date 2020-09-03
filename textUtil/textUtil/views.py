

#i have created this file-Adi
from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    # return HttpResponse("<h1>hey man</h1")
    return render(request, 'index.html')


def about(request):

    return HttpResponse("hi adi bhai")


def analyze(request):
    djtext=request.GET.get('text', 'default')

    removepunc=request.GET.get('removepunc', 'off')
    capitalise=request.GET.get('capitalise', 'off')
    
    punctuations=''';[]{},.""''()'''
    analyzed=""
    if(removepunc=="on"):
        for char in djtext:
            if(char not in punctuations):
                analyzed+=char
    else:
        analyzed=djtext
    if(capitalise=="on"):
        analyzed=analyzed.upper()



    params={ 'analyzed_text':analyzed}
    return render(request,'analyze.html',params)


def cap(request):

    return HttpResponse("The text has been capitalised")


def analyse(request):

    return HttpResponse("The analysis is here:")


def space(request):

    return HttpResponse("The spaces have been removed")


def lineremove(request):

    return HttpResponse("new line removed")

def charcount(request):

    return HttpResponse("have been counted")


