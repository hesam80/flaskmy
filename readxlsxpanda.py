from pandas import  read_excel
import numpy as np
df=read_excel('tst.xlsx',0)
tst=df.head()
sum_bedehkar=df['bedehkar'].sum()
print(tst)
print("sum_bedehkar is" ,sum_bedehkar)
min_bedehkar=np.min(df['bedehkar'])
print("min_bedehkar is ",min_bedehkar)
