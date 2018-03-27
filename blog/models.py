# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):

    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200, default='', blank=True)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre

class BonPlan(models.Model):

    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200, default='', blank=True)
    type = models.CharField(max_length=250)
    adresse = models.CharField(max_length=500)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre

class Video(models.Model):
    titre = models.CharField(max_length=200, default='')
    ybUrl = models.CharField(max_length=200, blank=True, default='https://www.youtube.com/embed/')
    ybId = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.titre

class Partenaire(models.Model):
    nom = models.CharField(max_length=250, default='')
    logo = models.ImageField(upload_to="logo/")
    url = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nom

class Description(models.Model):

    titre = models.CharField(max_length=200)
    contenu = models.TextField(null=True)

    def __str__(self):
        return self.titre
