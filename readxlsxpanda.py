from pandas import  read_excel
from configg import Configg
df=read_excel('tst.xlsx',0)
print(df)
d=Configg("hello")
print(d.s)
	
