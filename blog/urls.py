from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^accueil$', views.home, name='accueil'),
    url(r'^radio$', views.radio, name='radio'),
    url(r'^bonplans$',views.bonplans, name='bonplans'),
    url(r'^bonplan/(\d+)$', views.bonplan, name='bonplan'),
    url(r'^articles$', views.articles, name='articles'),
    url(r'^article/(\d+)$', views.article, name='article'),
    url(r'^videos$', views.videos, name='videos'),
    url(r'^partenaires$', views.partenaires, name='partenaires'),
]
