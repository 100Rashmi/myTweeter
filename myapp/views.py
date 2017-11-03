# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    text = "hello ! Everyone, this is my 1st project."
    return HttpResponse(text)
    # return render(request, "myapp/template/hello.html", {})

def morning(request):
    text = "good morning!!"
    return HttpResponse(text)