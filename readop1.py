import os, re, shutil , requests
from pandas import  read_excel
import numpy as np
from bs4 import BeautifulSoup

class Colors:
	""" IN ORDER TO USE COLORS OR SOME STYLING OPTIONS WE SHOULD USE THESE CONTANTS EASILY! """
	HEADER = '\034[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print(f"{Colors.HEADER}{Colors.BOLD}************************************************{Colors.ENDC}")
	print(f"{Colors.HEADER}{Colors.BOLD}*****  Hello - Hessam Hosseini  ******{Colors.ENDC}")
	print(f"{Colors.HEADER}{Colors.BOLD}************************************************{Colors.ENDC}")
	selected = input(f"""{Colors.WARNING}WHICH ONE? (1-2) {Colors.ENDC}
	1) RUN pandas_practce
	2) RUN op_one
	3) RUN task to do
	4) RUN tahlil_defect
	5) RUN tahlil_defect_op1
	6) RUN scrabbling
	7) RUN myscrabing
	8) Run APIs
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		pandas_practce(op_one)
	elif selected=="2":
		op_one()
		#print(op_one())
	elif selected=="3":
		pandas_practce(op_one)
		task_to_do()
	elif selected=="4":
		tahlil_defect_op1()
	elif selected=="5":
		tahlil_defect()
	elif selected=="6":
		scraping()
	elif selected=="7":
		myscraping()
	elif selected=="8":
		myapi()

def op_one():
	df=read_excel('op1.xlsx',0)
	return df['Chapter'].std()
	#tst1=df1.head()
	#print("sort date",date_sort)
	#tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	#print(df.dtypes)
	#print(df.count())
def pandas_practce(op_one):
	date=op_one()
	print("sort",date)


def task_to_do():
	tasks=[
	'sleep early in night',
	'works regurallity',
	'make a plan for days',
	'exercize',
	'review my weblog',
	'study python',
	]
	answers=[]
	rank=0
	percentage=100/len(tasks)
	for task in tasks:
		answer=input("Did you"+task + "?"+"(y or n)")
		answers.append(answer)
		if answer=="y":
			rank+=percentage
	
	print("you've done "+ str(int(rank))+ " % of your tasks")

def tahlil_defect_op1():
	df=read_excel('op1.xlsx',0)
	#for i in range(27,30):
	action=df['Action'][6]
	print(action)
	filter_tag=action[(int(action.find('P/N OFF:'))):]
	#filter_tag.find('P/N OFF:')
	filter_1st= filter_tag.replace('P/N OFF:', '')
	filter_2nd= filter_1st.replace('S/N OFF:', '')
	filter_3nd= filter_2nd.replace('P/N ON:', '')
	filter_4nd= filter_3nd.replace('S/N ON:', '')
	expose= filter_4nd[int(filter_4nd.find('P/N'))+9:].strip()
	x =expose.split()
	
	print(x,len(expose))
	

def tahlil_defect():
	
	
	tag="""AFTER T/S FOUND DUC TEMP SENSOR FAULTY , SO REPLACED WITH S/P IAW AMM 21-60-21 P 201 CHECK FOUND OK.
P/N Name: SENSOR
P/N OFF:4372C000
S/N OFF:244185-3
P/N ON:4372C000
S/N ON:1195

."""
	multi = """REFER TO ADDR #205522 APU STARTER REPLACED WITH SB PART IAW AMM 49-40-35 PB 201 FOUND SAT
P/N Name:
P/N OFF:519892-6-2
S/N OFF:11-4638
P/N ON:519892-6-2
S/N ON:11-4638
."""

	#length=len(tag)
	#print(tag+str(length))
	filter_tag=tag[(-1)*(int(tag.find('P/N OFF:'))):]
	#filter_tag.find('P/N OFF:')
	filter_1st= filter_tag.replace('P/N OFF', '')
	filter_2nd= filter_1st.replace('S/N OFF', '')
	filter_3nd= filter_2nd.replace('P/N ON', '')
	filter_4nd= filter_3nd.replace('S/N ON', '')
	

	#print(filter_tag.replace('P/N ON:', ''))
	print("Replace string is:",filter_tag)
	print("toole string",len(tag))
	pnnumber=(-1)*(int(filter_4nd.find('P/N')-8))
	#pnnumber+=8
	print(filter_4nd[int(filter_4nd.find('P/N'))+9:].strip())
	print(len(('P/N OFF:')))
	return filter_4nd[int(filter_4nd.find('P/N'))+9:].strip()

def scraping():
	#soap=BeautifulSoup('https://pythonspot.com/read-excel-with-pandas/','htmlparser')
	page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
	soup = BeautifulSoup(page.content, 'html.parser')
	seven_day = soup.find(id="seven-day-forecast")
	forecast_items = seven_day.find_all(class_="tombstone-container")
	#tonight = forecast_items[0]
	print("<html><h3>daily weather</h3>")
	for i in range(int(3)):
		tonight=forecast_items[i]
		print(tonight.prettify())
		i+=1
		
	#print(tonight.prettify())
	print("{}{}{}{}{}{}")
	print('home', 'user', 'documents', sep='/')
	#page2=requests.get('https://www.bbc.com/persian/magazine-52996956')
	#soup2=BeautifulSoup(page2.content,'htmlparser')
def myscraping():
	page=requests.get("https://www.bbc.com/persian/magazine-51502606")
	soup=BeautifulSoup(page.content,'html.parser')
	link = soup.findAll("a")
	print("Content-Type: text/html\n charset:utf-8\n")
	print(link[0].prettify())
	print(link[0].prettify())

def myapi():
	url="http://search.twitter.com/search.json?q=jQuery&result_type=recent&rpp=3"
	asd=requests.get(url)
	print(asd)

#task_to_do()
#op_one()
#pandas_practce(op_one)
display_menu()