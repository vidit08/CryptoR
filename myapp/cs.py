import pickle
from models import *
def currency_source_score():

	tier1 = pickle.load(open("tier1","rb"))
	tier2 = pickle.load(open("tier2","rb"))
	tier3 = pickle.load(open("tier3","rb"))
	tier4 = pickle.load(open("tier4","rb"))
	tier5 = pickle.load(open("tier5","rb"))

	currList = pickle.load(open("currNameList.pickle","rb"))

	final_dict={}

	for c in currList:
		final_dict[c] = [0,0,0,0,0] 


	def fill_dict(value,tier):
		if value in final_dict:
			print "here"
			final_dict[value][tier-1] += 1

	for x in tier1:
		query = 'SELECT Distinct currency_name,link,title,1 as id from currency_news WHERE link LIKE "%%' + x  + '%%"'

		result = Value.objects.raw(query)

		for y in result:
			fill_dict(y.currency_name,1)

	for x in tier2:
		query = 'SELECT Distinct currency_name,link,title,1 as id from currency_news WHERE link LIKE "%%' + x  + '%%"'

		result = Value.objects.raw(query)

		for y in result:
			fill_dict(y.currency_name,2)

	for x in tier3:
		query = 'SELECT Distinct currency_name,link,title,1 as id from currency_news WHERE link LIKE "%%' + x  + '%%"'

		result = Value.objects.raw(query)

		for y in result:
			fill_dict(y.currency_name,3)

	for x in tier4:
		query = 'SELECT Distinct currency_name,link,title,1 as id from currency_news WHERE link LIKE "%%' + x  + '%%"'

		result = Value.objects.raw(query)

		for y in result:
			fill_dict(y.currency_name,4)

	for x in tier5:
		query = 'SELECT Distinct currency_name,link,title,1 as id from currency_news WHERE link LIKE "%%' + x  + '%%"'

		result = Value.objects.raw(query)

		for y in result:
			fill_dict(y.currency_name,5)



	print final_dict		
	pickle.dump(final_dict,open("currency_source_score.p",'wb'))