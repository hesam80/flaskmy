from pandas import  read_excel
import numpy as np

def arzyabi():
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


def op_one():
	df=read_excel('op1.xlsx',0)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	print(df.dtypes)

#op_one()
arzyabi()