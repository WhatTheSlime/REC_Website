# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BonPlan
from blog.models import Article
from blog.models import Video
from blog.models import Partenaire
from .forms import ContactForm, ArticleForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    articles = Article.objects.all()
    videos = Video.objects.all()
    return render(request, 'home.html', {'derniers_articles': articles, 'dernieres_videos': videos})

def radio(request):
    return render(request, 'radio.html')

def bonplans(request):
    bonplans = BonPlan.objects.all()
    return render(request, 'bonplans.html', {'derniers_bonplans': bonplans})

def bonplan(request, id):
    """ Afficher un article complet """
    bonplan = get_object_or_404(Article, id=id)
    return render(request, 'bonplan.html', {'bonplan': bonplan})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'derniers_articles': articles})

def article(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})

def videos(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'dernieres_videos': videos})

def partenaires(request):
    partenaires = Partenaire.objects.all()
    return render(request, 'sponsors.html', {'partenaires': partenaires})
