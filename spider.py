import requests
import re
from bs4 import BeautifulSoup

targetUrl = "https://test.com"
foundLinks = []

def get_source(url):
	response = requests.get(url)
	source = BeautifulSoup(response.text,"html.parser")
	return source

def crawl(url):
	links = get_source(url)

	#for link in links.find_all('a'):

	for link in links.find_all('a',attrs={'href': re.compile("^https://")}):
		link = link.get("href")

		if link:
			
			if "#" in link:
				link = link.split("#")[0]

			if targetUrl in link and link not in foundLinks:
				foundLinks.append(link)
				print ("Found url --->",link)
				crawl(link)

crawl(targetUrl)
