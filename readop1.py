from pandas import  read_excel
import pandas as pd
import numpy as np




def op_one():
	df=read_excel('op1.xlsx',0)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	print(df.dtypes)

def op1_analize(file):
	df=read_excel('file',0)
	return df['Chapter'].std()
	tst1=df1.head()
	print("sort date",date_sort)
	#tst=df.head()
	#dp=df.groupby('Chapter').size()
	#print(dp)
	#print(df.dtypes)
	#print(df.count())
def pandas_practce():
	date=op_one()
	print("sort",date)


#op_one()
#op1_analize(file)
pandas_practce()