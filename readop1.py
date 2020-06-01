from pandas import  read_excel
import numpy as np

def arzyabi():
	arz=[
	'exercize',
	'business',
	'study',
	'python',
	]
	answers=input(f"do you done"+ arz + "(y or n)")
	count=0
	for answer in answers:
		if answer=='y':
			count+=1
	print(count)


def op_one():
	df=read_excel('op1.xlsx',0)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	print(df.dtypes)

#op_one()
arzyabi()