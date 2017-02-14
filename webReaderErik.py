import requests
from bs4 import BeautifulSoup
import re
import sys
import unicodedata
import time
class Hit:
    def __init__(self, date, name, link):
    	self.date = date
    	self.name = name
    	self.link = link

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}

prevRes = 10
curr = 0
links = []
while (prevRes == 10):
	time.sleep(5) # delays for 5 seconds

	response = requests.get("http://www.google.se/search?&tbm=nws&q=" + sys.argv[1] + "&start=" + (str(curr)), headers = headers)
	response.raise_for_status()

	soup = BeautifulSoup(response.text, "lxml")
	data = soup.findAll('div',attrs={'class':'g'})

	for div in data:
		#print("DIV " + str(div))
		desc = div.find('div', attrs={'class': 'st'}).text
		name = div.find('a').text
		link = div.find('a')['href'][7:]
		second = div.find('span', attrs={'class' : 'f'}).text
		links.append(Hit(second, name, link))
	prevRes = len(data)
	curr += prevRes

for link in links:
    print((link.name + "; " + link.date + "; " + link.link).encode('utf-8'))

print (str(len(links)) + " results");
print ("Data displayed as: Title; Date; Link")