from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post , Category

def home (request):
    
   
    return render(request,'blog/home.html')
