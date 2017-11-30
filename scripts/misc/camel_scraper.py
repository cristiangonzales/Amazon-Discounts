import requests
from bs4 import BeautifulSoup
import re, os
#example amazon url: https://www.amazon.com/EVGA-Optimized-Interlaced-Graphics-11G-P4-6393-KR/dp/B06Y11DFZ3/ref=sr_1_2?ie=UTF8&qid=1509044218&sr=8-2&keywords=nvidia+gtx+1080ti
#corresponding camelcamelcamel url: https://camelcamelcamel.com/EVGA-Optimized-Interlaced-Graphics-11G-P4-6393-KR/product/B06Y11DFZ3
def trim_amazon_url(url):
	#reg = re.search(url)
	pattern = "https:\/\/www.amazon.com\/.*\/dp\/.*\/"
	result = re.search(pattern,url)
	strResult = result.group(0)
	strResult = strResult.strip("https://www.amazon.com/")
	strResult = strResult.replace("dp", "product")
	#print "result is "
	#print strResult
	return strResult

def scrape_camel(amazonUrl):

	url = 'https://camelcamelcamel.com/' + trim_amazon_url(amazonUrl)
	try:
		response = requests.get(url)
		html = response.content

		soup = BeautifulSoup(html)
		table = soup.find('tbody', attrs={'class': 'stripe'})

		listOfRows = []
		for row in table.findAll('tr'):
		    listOfCells = []
		    for cell in row.findAll('td'):
		        text = cell.text.replace('&nbsp;', '')
		        listOfCells.append(text)
		    listOfRows.append(listOfCells)

		print listOfRows
		return listOfRows
	except Exception as e:
		print "Error: unable to connect to " + url + "for scraping. Error " + e.value

scrape_camel("https://www.amazon.com/EVGA-GeForce-GAMING-GDDR5X-Technology/dp/B06Y15DWXR/ref=sr_1_4?s=pc&ie=UTF8&qid=1511994768&sr=1-4&keywords=1080+ti")
