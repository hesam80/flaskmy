import os, re, shutil
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
    PLEASE SPECIFIE WITH A NUMBER: 
    """)
    if selected=="1":
    	pandas_practce(op_one)
    elif selected=="2":
    	op_one()
    	#print(op_one())
    elif selected=="3":
    	pandas_practce(op_one)
    	task_to_do()
    elif selected=="4":
    	tahlil_defect()
    elif selected=="5":
    	tahlil_defect_op1()

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
	for i in range(27,30):
		action=df['Action'][i]
		print(i,action)
	print(len(action))
	tahlil_action=action[-70:]
	print(tahlil_action)

def tahlil_defect():
	
	
	tag="""DURING ENG RUN UP FOUND ENG#4 IDLE PARAMETER OUT OF LIMIT SO HMU CHANGED IAW AMM 73-20-01 P401.

P/N OFF:2-193-330-13
S/N OFF:99AGU840
P/N ON:2-193-330-10
S/N ON:4AGU223."""
	multi = """DPFI FND TYRE #3 WAS FLAT AND NO GROOVE SO REPLACED BY NEW ONE IAW AMM 32-42-11 PB 401
P/N Name:NOSE WHEEL ASSY
P/N OFF:AHA1489
S/N OFF:ND116
P/N ON:AHA1480
S/N ON:NW097
."""
	text = (
    "%d little pigs come out, "
    "or I'll %s, and I'll %s, "
    "and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))
	#length=len(tag)
	#print(tag+str(length))
	filter_tag=multi[-70:]
	filter_tag.find('P/N OFF:')
	filter_1st= filter_tag.replace('P/N OFF:', '')
	filter_2nd= filter_tag.replace('S/N OFF:', '')
	#print(filter_tag.replace('P/N ON:', ''))
	print(filter_1st+filter_2nd)
	#print(text)

 	#<class 'bs4.element.Tag'>


#task_to_do()
#op_one()
#pandas_practce(op_one)
display_menu()