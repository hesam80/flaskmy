import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt
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
	6) RUN str practice
	7) RUN weibull_predict
	8) Run new_analyze
	9) Run sendsms BTC pass
	PLEASE SPECIFIE WITH A NUMBER: 
	""")
	print("select Number is:",selected)
	if selected=="1":
		pandas_practce()
	elif selected=="2":
		#insert_to_excel()
		print(op_one())
	elif selected=="3":
		pandas_practce()
fig, ax = plt.subplots(1, 1)