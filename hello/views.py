from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def name(request):
    return HttpResponse('<h2>Hello, <span style="color:red;">Asia</spap></h2>')

def hi(request):
    return HttpResponse("!DOCTYPE html<html><head></head><body></body></html>")

def hi2(request):
    return render(request, 'hi.html')

