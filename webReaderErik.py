import requests
from bs4 import BeautifulSoup
import re
import sys
import unicodedata

class Hit:
    def __init__(self, date, name, link):
    	self.date = date
    	self.name = name
    	self.link = link

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

response = requests.get("http://www.google.se/search?&tbm=nws&q=" + sys.argv[1], headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

data = soup.findAll('div',attrs={'class':'g'})

links = []
for div in data:
	first = re.search("<span class=\"f\">.*-.*</span></div><div class=\"st\"", str(div)).group(0)
	second = re.search("-.*</s", first).group(0)
	third = second[2:]
	fourth = third[:-3]
	#print("TOPRINT:" + fourth)
	#print("DIV: " + str(div))
	links.append(Hit(fourth, div.find('a')['href']));
	#for link in div.findAll('a'):
	#	links.append(link.get('href'));

for link in links:
    print("\n" + link.name + " " + link.date)

print (str(len(links)) + " results");