from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from first_app.models import AccessRecord,Topic,WebPage,User
# Create your views here.

def first(request):
    return HttpResponse("Hello World")

def baseimg(request):
    return render(request,'first_app/img.html')

def index(request):
    webpage = AccessRecord.objects.order_by('date')
    web_dict = {'acc_record':webpage}
    return render(request,'first_app/index.html',context=web_dict)

def help(request):
    help_dict = {'help_insert':"Welcome to help page"}
    return render(request,'first_app/index.html',context=help_dict)

def user(request):
    usrpage = User.objects.order_by('fname')
    usr_dict = {'usr_record':usrpage}
    return render(request,"first_app/index2.html",context=usr_dict)
