import os, re, shutil , requests , sendsms , time
import pandas as pd
from pandas import  read_excel
import numpy as np
import openpyxl


def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print("************************************************")
	print("*****  Hello - Hessam Hosseini  ******")
	print("************************************************")
	selected = input(f"""WHICH ONE? (1-8)
	1) RUN writing into file
	2) RUN insert into excel
	3) RUN task to do
	4) RUN tahlil_defect_op1
	5) RUN tahlil_defect
	6) RUN whatsup
	7) RUN myscrabing
	8) Run APIs
	9) Run sendsms BTC pass
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		title=input(f'insert title for search:  ')
		wiki_api(title)
	elif selected=="2":
		wiki_api2()
		
	elif selected=="3":
		pass
	elif selected=="4":
		pass
	elif selected=="5":
		pass
	elif selected=="6":
		pass
	elif selected=="7":
		pass
	elif selected=="8":
		pass



def wiki_api(title):
	url=f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch='+title+'&format=json'
	response=requests.get(url).json()
	url2="https://en.wikipedia.org/w/api.php"
	parameters={
	"action":"query",
	"format":"json",
	"list":"search",
	"srsearch": title
	}
	x=1
	response2=requests.get(url=url2,params=parameters).json()
	for i in range(2):
		result = response2['query']['search'][i]['snippet']
		finding='</span>'
		filters=int(result.find(finding)+7)
		if filters==-1:
			print("find not found",filters)
		else:
			
			print(i+int(1),"-",title+result[filters:]+"\n")

			
	

def wiki_api2():
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	SEARCHPAGE = "Black"
	PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHPAGE
    }
	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	if DATA['query']['search'][0]['title'] == SEARCHPAGE:
		print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")
		print(DATA['query']['search'][0]['snippet'])

display_menu()