import requests
from bs4 import BeautifulSoup
import re, os

def scrape_goldbox(discount):
	#loop through each page:
	asins = scrape_page('https://www.amazon.com/gp/goldbox')
	#hits = {}
	#for item in asin:
	#	get_camel_price(item)
	#	get_amazon_price(item)
	#	calculate discount
	#	if itemDiscount >= discount:
	#		hits.append(item)
	#return hits
	print asins
	return asins

def scrape_page(url):
	try:
		response = requests.get(url)
		html = response.content

		soup = BeautifulSoup(html, "html.parser")
		strOfContent = str(soup)
		#pattern = "\"reviewAsin.*\","
		pattern = "/dp/[0-9|A-Z]{9,11}"
		result = re.findall(pattern,strOfContent)
		for i in range(len(result)):
			item = result[i].replace("/dp/","")
			result[i] = item
		result = list(set(result))
		#print result
		return result
	except Exception as e:
		print "Error: unable to connect to " + url + "for scraping. Error "

scrape_goldbox(10)