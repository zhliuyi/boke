from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
def index(request):
    name='哈士奇'
    # return  HttpResponse()
    return render(request,'index.html',{'name':name})