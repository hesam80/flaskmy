import os, re, shutil , requests , sendsms
import pandas as pd
from pandas import  read_excel
import numpy as np
from bs4 import BeautifulSoup
import openpyxl


def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print("************************************************")
	print("*****  Hello - Hessam Hosseini  ******")
	print("************************************************")
	selected = input(f"""WHICH ONE? (1-8)
	1) RUN pandas_practce
	2) RUN op_one
	3) RUN task to do
	4) RUN tahlil_defect
	5) RUN tahlil_defect_op1
	6) RUN scrabbling
	7) RUN myscrabing
	8) Run APIs
	9) Run sendsms BTC pass
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		pandas_practce()
	elif selected=="2":
		op_one()
		#print(op_one())
	elif selected=="3":
		pandas_practce()
		task_to_do()
	elif selected=="4":
		tahlil_defect_op1()
	elif selected=="5":
		tahlil_defect()
	elif selected=="6":
		pass
	elif selected=="7":
		pass
	elif selected=="8":
		pass


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
def pandas_practce():
	date=tahlil_defect_op1()
	print("sort",date[0])
	#path = 'op1.xlsx'
	df = pd.DataFrame([[date[0], date[1], date[2]]],
              columns=['sn off','pn off','sn on'])
	print(df)

	
	#df.to_excel('H:\op1.xlsx',sheet_name='Sheet1')

	# with pd.ExcelWriter('H:\op1.xlsx') as writer:
	#  	writer.book = openpyxl.load_workbook('H:\op1.xlsx')
	#  	df.to_excel(writer, sheet_name='Sheet2')


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
	return x
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


#task_to_do()
#op_one()
#pandas_practce(op_one)
display_menu()