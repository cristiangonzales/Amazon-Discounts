import re, os
import time
import random
from selenium import webdriver


def unicode_to_ascii(listOfStr):
	for i in range(len(listOfStr)):
		asciiStr = listOfStr[i].encode('utf-8', errors='backslashreplace')
		listOfStr[i] = asciiStr
	return listOfStr
def scrape_goldbox(numOfPages):
	driver = webdriver.Chrome()
	driver.get("https://www.amazon.com/gp/goldbox")
	asins = []
	j = 0
	while(j<numOfPages):
		strOfContent = driver.page_source
		#try:
		pattern = "/dp/[0-9|A-Z]{9,11}"
		result = re.findall(pattern,strOfContent)
		for i in range(len(result)):
			item = result[i].replace("/dp/","")
			result[i] = item
		result = list(set(result))
		asins = asins + result
		# except Exception as e:
		# 	print "Error: unable to connect to " + url + "for scraping. Error "
		next_button = driver.find_elements_by_partial_link_text('Next')[0]
		driver.execute_script("window.scrollTo(0,4687)")
		next_button.click()
		j += 1
		time.sleep(random.random()*10)
	driver.close()
	driver.quit()
	#print unicode_to_ascii(asins)
	actualAsins = unicode_to_ascii(asins)
	#print type(actualAsins[0])
	return unicode_to_ascii(asins)
#scrape_goldbox(1)