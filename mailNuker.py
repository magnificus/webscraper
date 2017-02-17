import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import sys
import unicodedata
import time
import random

from selenium import webdriver


searchbase = ['free', 'register', 'hot', 'cool', 'premium', 'local', 'for', 'sign+up', 'free', 'money', 'register', 'newsletter', 'design', 'clean', 'performance', 'new', 'speed', 'global', 'mail', 'email', 'recieve', 'service', 'customer', 'news', 'tools', 'snacks', 'newsletter']

not_interesting = ['microsoft', 'youtube', 'google']

latest = None
def getSearch():
	totString = ""
	for i in range (random.randint(1,15)):
		totString += "+" + random.choice(searchbase)
	return totString

def getGoogleAddress():
	return "http://www.bing.com/search?q=" + getSearch()# + "+newsletter+email"


def tryInput():
	mailfields = driver.find_elements_by_xpath("//input[@type='text' or @type='email']");
	passfields = driver.find_elements_by_xpath("//input[@type='password']");
	latest = None
	
	print ("mailfields: " + str(len(mailfields)) + " passfields: " + str(len(passfields)))
	for element in mailfields:
		try:
			element.send_keys(mail)
			latest = element
		except:
			pass
		
	for element in passfields:
		try:
			element.send_keys(password)
			latest = element
		except:
			pass
	
	subscribebuttons = (driver.find_elements_by_xpath("//*[contains(text(), 'subscribe')]"))
	couldClick = False
	for i in subscribebuttons:
		try:
			i.click()
			couldClick = True
			break
		except:
			pass

	if not couldClick and latest:
		try:
			latest.submit()
		except:
			pass
		
			
def signUp():
	print("\nsigning up at: " + currentSite)
	response = requests.get(currentSite, headers = headers)
	soup = BeautifulSoup(response.text, "lxml")
	
	tryInput()

	return;


mail = sys.argv[1]
password = "!AYYasdds&&¤£34Sds"
driver = webdriver.Chrome()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'
}

toVisit = []

currentSite = getGoogleAddress()
toVisit.append(currentSite)
count = 0
while(True):
	count+=1
	if (len(toVisit) < 1 or count % 5 == 0):
		#randomize new address
		currentSite = getGoogleAddress()
		driver.quit()
		driver = webdriver.Chrome()
		toVisit = []
	else:
		currentSite = toVisit.pop()

	response = requests.get(currentSite, headers = headers)
	soup = BeautifulSoup(response.text, "lxml")
	driver.get(currentSite)

	# Retrieve potential new links for further jumps
	for link in soup.findAll('a'):
		if (random.randrange(1,5) == 1 and link.has_attr('href') and len(toVisit) < 100 and link['href'].startswith("http")) and "google" not in str(link) and "youtube" not in str(link) and "microsoft" not in str(link):
			#print ("adding: " + link['href'])
			toVisit.append(link['href'])
			
	# find interesting areas (register-buttons)
	interesting = (driver.find_elements_by_xpath("//*[contains(text(), 'sign in')]"))
	interesting += (driver.find_elements_by_xpath("//*[contains(text(), 'register')]"))
	interesting += (driver.find_elements_by_xpath("//*[contains(text(), 'subscribe')]"))

	signUp()
	for i in interesting:
		#print ("Found interesting link: " + str(i))
		couldClick = False
		try:
			i.click()
			couldClick = True
		except:
			pass
			#print ("could not press button for some reason :/")
		if couldClick:
			signUp()
			break

		
driver.quit()


