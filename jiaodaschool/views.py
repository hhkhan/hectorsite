# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, this page is jiaodaschool index page.")