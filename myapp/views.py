# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from myapp.models import Value
import requests
import json
# Create your views here.


class index(TemplateView):
    def get(self, request, **kwargs):

    	# currency = Value.objects.all();
    	# for c in currency:
    	# 	print c.currency_name
        
        response = requests.get("https://www.worldcoinindex.com/apiservice/json?key=g4TTyqrc3DbXvMlAx5QGvJHnyzDcf8")


        data =json.loads(json.dumps(response.json()))
       	currency_dict = {}
       	for entry in data['Markets']:
       		currency_dict[entry['Name']] = [entry['Label'], entry['Price_btc'] , entry['Price_usd'] , entry['Volume_24h']]

       	print currency_dict
        return render(request, 'index.html', context=None)