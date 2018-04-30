# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from myapp.models import Value
import requests
import json
import numpy as np
import pickle
# Create your views here.

from cs import currency_source_score
from rating_web import rate_website

class index(TemplateView):
    def get(self, request, **kwargs):
        response = requests.get("https://api.coinmarketcap.com/v1/ticker/")
        responseJSON = json.loads(json.dumps(response.json()))
        out = ''
        cnt = 0
        coinheatDict = {}
        for i in responseJSON:
            out = out + i['symbol'] + ','
            cnt = cnt + 1
            if cnt == 10:
                out = out[:-1]
                coinheatJSON = requests.get("https://chasing-coins.com/api/v1/std/coinheatmulti/" + out).json()
                for key in coinheatJSON:
                    coinheatDict[key] = coinheatJSON[key]
                cnt = 0
                out = ''
        out = out[:-1]
        coinheatJSON = requests.get("https://chasing-coins.com/api/v1/std/coinheatmulti/" + out).json()
        for key in coinheatJSON:
            coinheatDict[key] = coinheatJSON[key]

        for i in responseJSON:
            i['coinheat'] = coinheatDict[i['symbol']]

        try:
            movingAverageDict = pickle.load(open("movingAverage.pickle", "rb"))
            for i in responseJSON:
                priceList = movingAverageDict.get(i['symbol'], [265.002425, 275.2121])
                numList = np.array(priceList)
                i['standardDev'] = round(np.std(numList), 4)
                if len(priceList) == 0:
                    print(i['name'])
                    i['movingAverage'] = (265.002425 + 275.2121)/2
                else:
                    tempSum = 0
                    count = 0
                    for p in xrange(0, len(priceList), 7):
                        tempSum += priceList[p]
                        count = count + 1
                    if tempSum != 0:
                        i['movingAverage'] = round(tempSum/count, 4)
                    else:
                        i['movingAverage'] = 0

        except (OSError, IOError) as e:
            movingAverageDict = {}
            for i in responseJSON:
                temp = i['name'].split()
                if len(temp) > 1:
                    temp[1] = temp[1].lower()
                    temp = temp[0] + temp[1]
                else:
                    temp = temp[0]
                ##Difference in name and stored name
                if i['name'] == 'Stellar':
                    temp = 'Stellarlumens'
                elif i['name'] == 'Basic Attention Token':
                    temp = 'Bat'
                elif i['name'] == 'Waltonchain':
                    temp = 'Walton'
                elif i['name'] == 'Kyber Network':
                    temp = 'Kyber'
                elif i['name'] == 'Byteball Bytes':
                    temp = 'Byteball'

                tempTuples = Value.objects.raw('''SELECT *,1 as id FROM CryptoNews.Value where currency_name = %s AND time >= NOW() + INTERVAL -7 DAY AND time <  NOW() + INTERVAL  0 DAY;''', [temp])
                priceList = []
                for tuple in tempTuples:
                    priceList.append(tuple.quote)

                movingAverageDict[i['symbol']] = priceList
                numList = np.array(priceList)
                i['standardDev'] = round(np.std(numList), 4)

                tempSum = 0
                count = 0
                if len(priceList) == 0:
                    print(i['name'])
                    priceList = [265.002425, 275.2121]

                for p in xrange(0, len(priceList), 7):
                    tempSum += priceList[p]
                    count = count + 1
                i['movingAverage'] = round(tempSum/count, 4)

            with open('movingAverage.pickle', 'wb') as handle:
                pickle.dump(movingAverageDict, handle, protocol = pickle.HIGHEST_PROTOCOL)

        #calculate discussion index
        currencySrcScore = pickle.load(open("currency_source_score.p", "rb"))
        discussionIdx = 0
        currSrcScoreDict = {}
        for key, val in currencySrcScore.iteritems():
            discussionIdx = 10 * val[0] + 3 * val[1] + 2 * val[2] + val[3]
            currSrcScoreDict[key] = discussionIdx

        for i in responseJSON:
            #reward
            reward = i['movingAverage'] / float(i['price_usd']) * 100
            if reward > 95:
                reward = 5
            elif reward > 85 and reward <= 95:
                reward = 4
            elif reward > 75 and reward <= 85:
                reward = 3
            elif reward > 60 and reward <= 75:
                reward = 2
            else:
                reward = 1

            #risk
            risk = i['standardDev'] / float(i['price_usd']) * 100
            if risk > 9.5:
                risk = -5
            elif risk > 6.5 and risk <= 9.5:
                risk = -4
            elif risk > 3.5 and risk <= 6.5:
                risk = -3
            elif risk > 2.0 and risk <= 3.5:
                risk = -2
            else:
                risk = -1

            disIdx = currSrcScoreDict.get(i['name'], 1)
            if disIdx > 100:
                disIdx = 5
            elif disIdx > 75 and disIdx <= 100:
                disIdx = 4
            elif disIdx > 45 and disIdx <= 75:
                disIdx = 3
            elif disIdx > 25 and disIdx <= 45:
                disIdx = 2
            elif disIdx > 0 and disIdx <= 25:
                disIdx = 1
            else:
                disIdx = 0

            #main formula
            rating = risk + 1.25 * reward + 3 * disIdx

            ratingGrade = 'E'
            if rating > 7:
                ratingGrade = 'A'
            elif rating > 5 and rating <= 7:
                ratingGrade = 'B'
            elif rating > 3 and rating <= 5:
                ratingGrade = 'C'
            elif rating > 1 and rating <= 3:
                ratingGrade = 'D'
            i['ratingGrade'] = ratingGrade

            print(risk + reward + disIdx)

        return render(request, 'home.html', {'responseJSON': responseJSON})


class sources(TemplateView):
    def get(self, request, **kwargs):

    	# currency = Value.objects.all();
    	# for c in currency:
    	# 	print c.currency_name
        
		# response = requests.get("https://www.worldcoinindex.com/apiservice/json?key=g4TTyqrc3DbXvMlAx5QGvJHnyzDcf8")


		# data =json.loads(json.dumps(response.json()))
		
		# currency_dict = {}
		# for entry in data['Markets']:
		# 	currency_dict[entry['Name']] = [entry['Label'], entry['Price_btc'] , entry['Price_usd'] , entry['Volume_24h']]


		# crypto_table = json.dumps(currency_dict)
		# rate_website()


		# currency_source_score()

		with open('source_table.json') as fp:
			data = json.load(fp)

		return render(request, 'websource.html', {'table' : data })


class about(TemplateView):
    def get(self, request, **kwargs):


        return render(request, 'about.html')


def detail(request,currency):
    responseJSON = {}
    #get info has all the info
    response = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    # responseJSON = json.loads(json.dumps(response.json()))
    temp_dict = json.loads(json.dumps(response.json()))

    element = {}
    for x in temp_dict:
        if x["symbol"] == currency:
            element = x
            break
        # print x
        # break
    
    print element

    query = 'Select link,title,date,1 as id from CryptoNews.currency_news where currency_name = "'+ element["name"] +'" order by date desc limit 10'
    result = Value.objects.raw(query)

    news = []

    for x in result:
        news.append({'link' : x.link ,
            'title' : x.title,
            'date' : x.date.strftime('%m/%d/%Y')})

    print news

    #image part not working
    #requests.get("https://chasing-coins.com/api/v1/std/logo/" + key)
    image = "https://chasing-coins.com/api/v1/std/logo/" + currency
    return render(request,'currencyPage.html',{'responseJSON' : element,
        'image' : image ,
        'news' : news})