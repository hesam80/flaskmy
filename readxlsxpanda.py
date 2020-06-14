import pandas as pd
from pandas import  read_excel
from pandas import 
from configg import Configg

df = pd.read_excel('tst.xlsx',0)
df.head()	
e=df['bedehkar'].min()
print(e)