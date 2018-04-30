from django.db import connection
from models import *
import pickle
def rate_website():

	web_list = []
	with open('wikiMention.csv','r') as f:
		content = f.readlines()


	web_list = [x.strip().split(',') for x in content]
	web_list = sorted(web_list,key = lambda x: int(x[1]))
	print "length original list " + str(len(web_list))
	new_list = {}

	tier1 = []
	tier2 = []
	tier3 = []
	tier4 = []
	tier5 = []
  	max_articles = 0
	max_coverage = 0
	# print query_list
	index = 0
	for x in web_list:
		query = 'SELECT Distinct link,title,1 as id from currency_news WHERE link LIKE "%%' + x[0]  + '%%"'
		# print query
		result = Value.objects.raw(query)
		# for x in result:
		# 	print x


		l = 0
		for y in result:
			l+= 1

		if l>max_articles:
			max_articles = l				
		query = 'SELECT Distinct currency_name,1 as id from currency_news WHERE link LIKE "%%' + x[0]  + '%%"'
		result = Value.objects.raw(query)
		l1= 0 
		for y in result:
			l1 += 1

		if l1> max_coverage:
			max_coverage = l1	
		# print "l= " + str(l) +  " l1= " + str(l1)
		new_list[index] = {'name' : str(x[0]) ,'wiki_mentions': int(x[1]) , 'articles' : l ,'currency_coverage' : l1 ,'rating' : 0.0 }
		index += 1

	# print new_list
	def get_class(value):
		if value == 500:
			return 6
		elif value >100:
			return 3
		elif value > 10:
			return 2
		elif value> 0:
			return 1
		else:
			return 0

	def get_popularity(value,name):
		if value == 500:
			tier1.append(name)
			return "Tier 1"
		elif value >100:
			tier2.append(name)
			return "Tier 2"
		elif value > 10:
			tier3.append(name)
			return "Tier 3"
		elif value> 0:
			tier4.append(name)
			return "Tier 4"
		else:
			tier5.append(name)
			return "Tier 5"

	# print max_articles
	# print max_coverage

	for key, x in new_list.iteritems():
		y = (float(x['articles']) * float((2.0/max_articles)))
		z = (float(x['currency_coverage']) * float((2.0/max_coverage))) 
		temp = float(get_class(x['wiki_mentions']))  + y + z

		x['rating'] = format(temp,'.2f')
		# print y,z
		# print x['rating'],(x['articles'] * (3/max_articles)),(x['currency_coverage'] * (3/max_coverage)) 

		x['wiki_mentions'] = get_popularity(x['wiki_mentions'], x['name'])
	import json

	pickle.dump( tier1, open( "tier1", "wb" ) )
	pickle.dump( tier2, open( "tier2", "wb" ) )
	pickle.dump( tier3, open( "tier3", "wb" ) )
	pickle.dump( tier4, open( "tier4", "wb" ) )
	pickle.dump( tier5, open( "tier5", "wb" ) )
	with open('source_table.json', 'w') as fp:
  		json.dump(new_list, fp)




	# result = Cryptonews.objects.raw('SELECT link,title,1 as id from cryptonews WHERE link LIKE "' + x[0]  + '"') 


	# print len(list(result))
