import os, re, shutil , requests , sendsms , time
from flask import Flask

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
		write_file()
	elif selected=="2":
		pass
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
def write_file():
	print("hi")

display_menu()