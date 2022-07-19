from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h1>欢迎使用</h1>')
