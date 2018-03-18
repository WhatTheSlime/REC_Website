# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-16 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180315_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='urls',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='video',
            name='titre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='video',
            name='ybId',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='video',
            name='ybUrl',
            field=models.CharField(blank=True, default='https://www.youtube.com/iframe_api', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=200),
        ),
    ]