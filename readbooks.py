import requests
import bs4
import urllib3 as urlib
import logging

logging.basicConfig(level=logging.INFO)
# liste authors by name start A in wikipedia ro neshaan mide
def showbook(name):
	try:
		name=urlib.quote_plus(name)
		baseURL='https://www.goodreads.com'
		goodreads=requests.get(baseURL+"/search?utf8=%E2%9C%93&search_type=books&search%5Bfield=outhor&q="+name)
		soap= bs4.BeautifulSoup(goodreads.content,"html.paresr")
		firstbookURL=soap.find("a","bookTitle")['href']
		print(firstbookURL)
	except:
		pass

page= requests.get("https://en.m.wikipedia.org/wiki/List_of_authors_by_name:_M")
soap=bs4.BeautifulSoup(page.content,"html.parser")
names=soap.findAll("a")

for name in names:
	if name is None:
		print ("None")
		continue
	if len(str(name.string))>44:
		#print(name.string)
		print(len(str(name.string)))
		print(str(name.string))