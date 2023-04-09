from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from .decorators import *


def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}

    if request.method == "POST":
        if request.POST.get('search'):
            article_title = request.POST.get('search').lower()
            articles_by_title = Article.objects.filter(title__icontains=article_title)
            context = {'articles': articles_by_title, 'categories': categories}
            return render(request, 'home.html', context)
        if request.POST.get('category'):
            if request.POST.get('category') == 'All Categories':
                return render(request, 'home.html', context)
            category = request.POST.get('category')
            articles_by_category = Article.objects.filter(category_id=category)
            context = {'articles': articles_by_category, 'categories': categories}
            return render(request, 'home.html', context)
    # Authentication User
    if request.user.is_authenticated:
        group = request.user.groups.all()[0].name 
        context = {'articles': articles, 'categories': categories, 'group': group}
        return render(request, 'home.html', context)
    else:
        # login
        if request.POST.get('username') and request.POST.get('password'):
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                # check if user credentials are right
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    # A backend authenticated the credentials
                    login(request, user)
                    return redirect('home')
                else:
                # No backend authenticated the credentials
                    messages.info(request, 'Username or Password is incorrect!')
                    return redirect('home')
        else:
            return render(request, 'home.html', context)

def articleDetail(request, pk):
    article = Article.objects.get(article_id=pk)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

@allowed_users(allowed_roles=['managers', 'admins'])
def addArticle(request):
    if request.user.is_authenticated:
        form = Add_Article
        if request.method == 'POST':
            form = Add_Article(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'add_article.html', context)
    return redirect('home')

@allowed_users(allowed_roles=['managers', 'admins'])
def updateArticle(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(article_id=pk)
        form = Add_Article(instance=article)
        if request.method == 'POST':
            form = Add_Article(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'update_article.html', context)
    return redirect('home')

@allowed_users(allowed_roles=['admins'])
def deleteArticle(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(article_id=pk)
        article.delete()
        return redirect('home')
    return redirect('home')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    return redirect('home')