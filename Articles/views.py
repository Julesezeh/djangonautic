from gc import get_objects
from multiprocessing import context
from pyexpat import model
from re import template
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle, EditArticle 
from django.views.generic import UpdateView


# Create your views here.
def artyy(request):
    instance = Articles.objects.all().order_by('date')
    dictionary = {'Articles':instance}
    return render(request,'articles.html',context=dictionary)



def article_detail(request,slug):
    article = Articles.objects.get(slug=slug)
    dictionary = {'art':article}
    return render(request,'articles/article_detail.html',dictionary)



@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save form
            x = form.save(commit=False)
            x.author = request.user
            x.save()
            return redirect('particular:articles')
    else:
        form = CreateArticle()
    return render(request,'articles/create_article.html',{'form':form})


def edit_article(request,slug):
    article = Articles.objects.get(slug=slug)
    if request.method == 'POST':
        form = EditArticle(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('particular:articles')
    else:
        form = EditArticle(article,slug)
    print(article.date)
    return render(request,'articles/edit_article.html',context={'form':form})


class edit_article(UpdateView):
    model = Articles
    template_name = 'articles/edit_article.html' 
    fields = ['title','body']

def log_view(request,slug):
    article = Articles.objects.get(slug=slug)

