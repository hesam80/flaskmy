#!C:\xampp\htdocs\pythonpro\flaskmy\env\Scripts\python.exe
import pandas as pd
import numpy as np
def op_one():
	df=pd.read_excel('op1.xlsx',0)
	tst=df.head()
	dp=df.groupby('Chapter').size()
	print(dp)
	print(df.dtype())

op_one()