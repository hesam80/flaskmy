import requests
import bs4
import urllib3 as urlib
import logging

logging.basicConfig(level=logging.INFO)

def showbook(name):
	try:
		name=urlib.quote_plus(name)
		baseURL='https://www.goodreads.com'
		goodreads=requests.get(baseURL+"/search?utf8=%E2%9C%93&search_type=books&search%5Bfield=outhor&q="+name)
		soap= bs4.BeautifulSoup(goodreads.content,"html.paresr")
		frstbookURL=soap.find("a","bookTitle")['href']
		print(baseURL)
	except:
		pass

page= requests.get("https://en.m.wikipedia.org/wiki/List_of_authors_by_name:_M")
soap=bs4.BeautifulSoup(page.content,"html.parser")
names=soap.findAll("a")

for name in names:
	if name is None:
		print ("None")
		continue
	if len(str(name.string))>2:
		showbook(name)