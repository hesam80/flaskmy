from pandas import  read_excel
import numpy as np
def op_one():
	df=read_excel('op1.xlsx',0)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	print(df.dtypes)

op_one()