# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BonPlan
from blog.models import Article
from blog.models import Video
from blog.models import Partenaire
from blog.models import Description
from .forms import ContactForm, ArticleForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    bonplans = BonPlan.objects.all()
    articles = Article.objects.all()
    videos = Video.objects.all()
    descriptions = Description.objects.all()
    return render(request, 'home.html', {'derniers_bonplans': bonplans, 'derniers_articles': articles, 'dernieres_videos': videos, 'descriptions': descriptions})

def radio(request):
    descriptions = Description.objects.all()
    return render(request, 'radio.html', {'descriptions': descriptions})

def bonplans(request):
    bonplans = BonPlan.objects.all()
    descriptions = Description.objects.all()
    return render(request, 'bonplans.html', {'derniers_bonplans': bonplans, 'descriptions': descriptions})

def bonplan(request, id):
    bonplan = get_object_or_404(BonPlan, id=id)
    return render(request, 'bonplan.html', {'bonplan': bonplan})

def articles(request):
    articles = Article.objects.all()
    descriptions = Description.objects.all()
    return render(request, 'articles.html', {'derniers_articles': articles, 'descriptions': descriptions})

def article(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})

def videos(request):
    videos = Video.objects.all()
    descriptions = Description.objects.all()
    return render(request, 'videos.html', {'dernieres_videos': videos, 'descriptions': descriptions})

def partenaires(request):
    partenaires = Partenaire.objects.all()
    descriptions = Description.objects.all()
    return render(request, 'sponsors.html', {'partenaires': partenaires, 'descriptions': descriptions})
