from pandas import  read_excel
import numpy as np
def pdnp():
	df=read_excel('tst.xlsx',0)
	tst=df.head()
	sum_bedehkar=df['bedehkar'].sum()
	print(tst)
	print("sum_bedehkar is" ,sum_bedehkar)
	min_bedehkar=np.min(df['bedehkar'])
	print("min_bedehkar is ",min_bedehkar)
	max_mandeh=np.max(df['mandeh'])
	print("max_mandeh is ",max_mandeh)

def np_tst():
	Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
	print("z is:",z)



#pdnp()
np_tst()