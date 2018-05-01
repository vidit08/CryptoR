
import json


def updated():
	with open('wikiMention.csv','r') as f:
			content = f.readlines()


	web_list = [x.strip().split(',') for x in content]
	web_list = sorted(web_list,key = lambda x: int(x[1]))


	new_list = [
				 ['ledgergazette.com', 10846],
				 ['stocknewstimes.com', 9722],
				 ['thelincolnianonline.com', 9529],
				 ['weekherald.com', 7747],
				 ['registrarjournal.com', 7660],
				 ['dispatchtribunal.com', 5324],
				 ['theenterpriseleader.com', 3562],
				 ['seekingalpha.com', 1305],
				 ['cointradejournal.com', 955],
				 ['investopedia.com', 878],
				 ['bangaloreweekly.com', 747],
				 ['rt.com', 723],
				 ['businessinsider.com', 574],
				 ['markets.businessinsider.com', 547],
				 ['sputniknews.com', 471],
				 ['investors.com', 453],
				 ['ambcrypto.com', 429],
				 ['btcmanager.com', 420],
				 ['huronreport.com', 401],
				 ['news.bitcoin.com', 399],
				 ['stl.news', 398],
				 ['cryptovest.com', 398],
				 ['themerkle.com', 395],
				 ['wolcottdaily.com', 393],
				 ['cointelegraph.com', 389],
				 ['utahherald.com', 381],
				 ['heraldks.com', 375],
				 ['invezz.com', 368],
				 ['flintdaily.com', 363],
				 ['en.brinkwire.com', 363],
				 ['santimes.com', 363],
				 ['mashable.com', 342],
				 ['weeklyhub.com', 313],
				 ['presstelegraph.com', 304],
				 ['coindesk.com', 303],
				 ['bloombergquint.com', 301],
				 ['kldaily.com', 294],
				 ['cnbc.com', 294],
				 ['cnet.com', 288],
				 ['cryptodaily.co.uk', 287],
				 ['smartereum.com', 271],
				 ['bobrtimes.com', 268],
				 ['forexlive.com', 266],
				 ['investorideas.com', 259],
				 ['theverge.com', 258],
				 ['independent.co.uk', 258],
				 ['gizmodo.com.au', 253],
				 ['weeklyregister.com', 253],
				 ['business.financialpost.com', 250],
				 ['bzweekly.com', 249],
				 ['valuewalk.com', 249],
				 ['ethereumworldnews.com', 244],
				 ['zdnet.com', 235],
				 ['hacked.com', 233],
				 ['inverse.com', 227],
				 ['baseballnewssource.com', 217],
				 ['irishtechnews.ie', 216],
				 ['techcrunch.com', 216],
				 ['pcgamer.com', 210],
				 ['reurope.com', 208],
				 ['fool.com', 205],
				 ['blocktribune.com', 203],
				 ['cryptona.co', 200],
				 ['cryptorecorder.com', 199],
				 ['bitsonline.com', 192],
				 ['coinidol.com', 191],
				 ['coinspeaker.com', 185],
				 ['fool.com.au', 179],
				 ['crowdfundinsider.com', 162],
				 ['slashgear.com', 161],
				 ['time.com', 159],
				 ['zycrypto.com', 158],
				 ['fortune.com', 157],
				 ['insidebitcoins.com', 152],
				 ['nigeriatoday.ng', 152],
				 ['slate.com', 151],
				 ['cryptoslate.com', 149],
				 ['livebitcoinnews.com', 146],
				 ['finder.com.au', 145],
				 ['cryptocurrencynews.com', 139],
				 ['mareainformativa.com', 139],
				 ['equitiesfocus.com', 137],
				 ['benzinga.com', 137],
				 ['thenextweb.com', 134],
				 ['pymnts.com', 134],
				 ['stocksgazette.com', 132],
				 ['crypto-lines.com', 125],
				 ['cryptocrimson.com', 121],
				 ['usethebitcoin.com', 118],
				 ['oracletimes.com', 118],
				 ['techrepublic.com', 105],
				 ['leaprate.com', 100],
				 ['ethnews.com', 98],
				 ['arstechnica.com', 97],
				 ['coincentral.com', 91],
				 ['motherboard.vice.com', 85],
				 ['coinjournal.net', 83],
				 ['siliconangle.com', 83],
				 ['americanbanker.com', 78],
				 ['themarketmogul.com', 71],
				 ['paymentssource.com', 70],
				 ['digitaltrends.com', 65],
				 ['kgazette.com', 60],
				 ['bleepingcomputer.com', 59],
				 ['newsbtc.com', 59],
				 ['hardocp.com', 59],
				 ['infosurhoy.com', 56],
				 ['computerweekly.com', 52],
				 ['recode.net', 52],
				 ['finnewsdaily.com', 51],
				 ['theusacommerce.com', 49],
				 ['crypto-reporter.com', 48],
				 ['normanobserver.com', 48],
				 ['hothardware.com', 46],
				 ['coinclarity.com', 45],
				 ['globalcryptopress.com', 45],
				 ['financemagnates.com', 43],
				 ['financefeeds.com', 40],
				 ['ibtimes.co.uk', 39],
				 ['chipin.com', 38],
				 ['realdaily.com', 37],
				 ['strategiccoin.com', 37],
				 ['globalcoinreport.com', 33],
				 ['nasdaq.com', 32],
				 ['dcebrief.com', 28],
				 ['news.finance.co.uk', 25],
				 ['news4c.com', 24],
				 ['bitcoinist.com', 23],
				 ['metro.co.uk', 22],
				 ['informationsecuritybuzz.com', 22],
				 ['micetimes.asia', 22],
				 ['marketwatch.com', 20],
				 ['digitaljournal.com', 19],
				 ['notebookcheck.net', 18],
				 ['bloomberg.com', 17],
				 ['marketbusinessnews.com', 15],
				 ['thestreet.com', 15],
				 ['prnewswire.com', 14],
				 ['express.co.uk', 14],
				 ['venturebeat.com', 11],
				 ['legalgamblingandthelaw.com', 11],
				 ['cbc.ca', 10],
				 ['ibtimes.com', 10],
				 ['smnweekly.com', 10],
				 ['fxstreet.com', 10],
				 ['equities.com', 9],
				 ['foxbusiness.com', 9],
				 ['uk.businessinsider.com', 8],
				 ['newsweek.com', 8],
				 ['businessinsider.com.au', 8],
				 ['thehill.com', 7],
				 ['theglobeandmail.com', 6],
				 ['investorplace.com', 6],
				 ['hadeplatform.com', 6],
				 ['tgdaily.com', 5],
				 ['econotimes.com', 5],
				 ['govtech.com', 5],
				 ['uk.finance.yahoo.com', 5],
				 ['wwnytv.com', 4],
				 ['jdsupra.com', 4],
				 ['emchat.net', 3],
				 ['dailytelescope.com', 3],
				 ['globenewswire.com', 2],
				 ['financialtribune.com', 2],
				 ['stockhouse.com', 2],
				 ['wsj.com', 2],
				 ['profitconfidential.com', 2],
				 ['moneymorning.com', 2],
				 ['icoexaminer.com', 2],
				 ['wccftech.com', 2],
				 ['financialbuzz.com', 1],
				 ['paymentweek.com', 1]]


	new_dict = {}

	for x in new_list:
		new_dict[x[0]] = x[1]

	def get_rating(value):
		if value == 500:
			# tier1.append(name)
			return "5"
		elif value >100:
			# tier2.append(name)
			return "4"
		elif value > 10:
			# tier3.append(name)
			return "3"
		elif value> 0:
			# tier4.append(name)
			return "2"
		else:
			# tier5.append(name)
			return "1"

	temp_list = {}
	print(new_dict)			 
	index = 0
	for x in web_list:
		if str(x[0]) in new_dict:
			# num_articles = new_dict(str(x[0]))
			new_dict[str(x[0])]
			temp_list[index] = {'name' : str(x[0]) ,'wiki_mentions': int(x[1]) , 'articles' : new_dict[str(x[0])]  ,'rating' : get_rating(int(x[1])) }
			index += 1

	with open('source_table_new.json', 'w') as fp:
  		json.dump(temp_list, fp)