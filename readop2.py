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
	1) RUN pandas_practce
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
		write_file()
	elif selected=="2":
		pass
		#print(op_one())
	elif selected=="3":
		pass
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


def write_file():
	f=open("tst1.txt","w+")
	for i in range(2):
		f.write("this line is:%d\r\n " %(i+1))
	f.close()


def insert_to_excel():
	date=tahlil_defect_op1()
	df1=pd.DataFrame(date)
	#print(df1)
	df=pd.DataFrame([date[0]])
	print(df[0])
	# book=openpyxl.load_workbook('op1.xlsx')
	# writer=pd.ExcelWriter('op1.xlsx', engine='openpyxl')
	# writer.book=book
	# writer.sheets={ws.title:ws for ws in book.worksheets}
	# print("maxrow is: ",writer.sheets['Sheet1'].max_row)
	#df.to_excel(writer, sheet_name='Sheet1', index=False)
	#append_df_to_excel('op1.xlsx', df,sheet_name='Sheet1', index=False, encoding='utf-8')
	


def tahlil_defect_op1():
	df=read_excel('op1.xlsx',0)
	for i in range(6,13):
		action=df['Action'][i]
		print(action)
		print(action.find('P/N OFF:'))
		if action.find('P/N OFF:') != '-1':
			filter_tag=action[(int(action.find('P/N OFF:'))):]
			#filter_tag.find('P/N OFF:')
			filter_1st= filter_tag.replace('P/N OFF:', '')
			filter_2nd= filter_1st.replace('S/N OFF:', '')
			filter_3nd= filter_2nd.replace('P/N ON:', '')
			filter_4nd= filter_3nd.replace('S/N ON:', '')
			expose= filter_4nd[int(filter_4nd.find('P/N'))+9:].strip()
			x =expose.split()
			i+=1
			x=pd.DataFrame(x)
			print(x)
			return x
		elif action.find('P/N OFF:') == '-1':
			#print("no part is changed")
			#print(x,len(expose))
			pass
	


	
	

def tahlil_defect():
	
	
	tag="""DUE TO REPORT OF CABIN LOG #59472 NEW PARTS PROVIDED AND INSTALLED IAW AMM 25-00-00
P/N Name:LIFT JACK 17D
P/N OFF:-
S/N OFF:-
P/N ON:41030001
S/N ON:9573447-065
."""
	multi = """FOR T/S FUEL FILTER REPLACED WITH S/B PART & ENG RUN UP PERFORMED IAW AMM 73-10-04 P401.

P/N OFF:2-310-073-01
S/N OFF:NIL
P/N ON:2-310-073-01
S/N ON:NIL
"""
	tease="""P/N Name:
P/N OFF:aha1489
S/N OFF:2712005
P/N ON:AHA1489
S/N ON:19956"""

	temp="""P/N Name:
P/N OFF:
S/N OFF:
P/N ON:
S/N ON:"""
	instance='this is a book'


	sentences=input(f"select multi or tag:  ")	
	if sentences=="multi":
		sentences=multi
	elif sentences=="temp":
		sentences=temp
	elif sentences=="tag":
		sentences=tag
	elif sentences=="instance":
		sentences=instance
	#length=len(tag)
	#print(tag+str(length))
	print("toole sentences is : ",(-1)*(int(len(sentences))))

	filter_tag=sentences[(-1)*(int(sentences.find('P/N OFF:'))):]
	# #filter_tag.find('P/N OFF:')
	# filter_1st= filter_tag.replace('P/N OFF:', '')
	# filter_2nd= filter_1st.replace('S/N OFF:', '')
	# filter_3nd= filter_2nd.replace('P/N ON:', '')
	# filter_4nd= filter_3nd.replace('S/N ON:', '')

	#print(filter_tag.replace('P/N ON:', ''))
	#print("Replace string is:",filter_4nd)
	#print("filter",filter_tag)
	#pnnumber=int(sentences.find('P/N OFF:'))
	#print(int(sentences.find('P/N OFF:')))
	#print(filter_4nd[pnnumber:])
	#pnnumber+=8
	#print(filter_4nd[int(filter_4nd.find('P/N'))+9:].strip())
	#print(len((filter_tag)))
	#return filter_4nd[int(filter_4nd.find('P/N'))+9:].strip()
	finding='IAW AMM'
	filters=int(sentences.find(finding))
	if filters==-1:
		print("find not found",filters)
	else:
		print("find book yes",filters)
		print(sentences[filters:])
	s=int(len(sentences)-1)
	i=0
	#for i in range(0,s):
		#print(sentences[i:s])
		#i+=1
		#print(sentences[-1*s:])
		#s-=1



#task_to_do()
#op_one()
#pandas_practce(op_one)
display_menu()