from pandas import  read_excel
import numpy as np
def op_one():
	df=read_excel('op1.xlsx',0)
	date_sort= df['Chapter'].std()
	#tst1=df1.head()
	print("sort date",date_sort)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	#print(dp)
	#print(df.dtypes)
	#print(df.count())
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

	print("you've done"+ str(rank)+ "% of your tasks")


#task_to_do()
op_one()