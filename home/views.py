from django.shortcuts import render
from .models import *

def home(request):

    context = {
        "articles":[art for art in Article.objects.all()][::-1]
    }

    return render(request,'home/home.html',context)

def about(request):
    return render(request,'home/about.html',{})

def article(request,name):

    for a in Article.objects.all():
        if a.author.first_name.lower() + a.author.last_name.lower() == name:
            article = a
            break

    context = {
        "article":article
    }

    return render(request,'home/article.html',context)
