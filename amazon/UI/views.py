from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def web(req):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())

def website(req):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())