from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def myresp(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html',{'articles':articles})
#
# def article_page(request):
#     article = models.Article.objects.get()