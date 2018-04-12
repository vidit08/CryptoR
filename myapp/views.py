# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from myapp.models import Value

# Create your views here.


class index(TemplateView):
    def get(self, request, **kwargs):

    	currency = Value.objects.all();
    	print currency
        return render(request, 'index.html', context=None)