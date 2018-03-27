# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article
from .models import BonPlan
from .models import Video
from .models import Partenaire
from .models import Description

# Register your models here.
admin.site.register(Article)
admin.site.register(BonPlan)
admin.site.register(Video)
admin.site.register(Partenaire)
admin.site.register(Description)
