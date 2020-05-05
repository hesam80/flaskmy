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
    # array shatranji 4 row 4 column
	z = np.tile( np.array([[0,1],[1,0]]), (4,4))
	print("z is:",z)

def np_tst2():
    # normalize karadane array
	Z = np.random.random((5,5))
	Zmax, Zmin = Z.max(), Z.min()
	Z = (Z - Zmin)/(Zmax - Zmin)
	print("Z and Zmax, Zmin: ", Z, Zmax , Zmin)
	today = np.datetime64('today', 'D')
	#today+=1
	print("today is: ",today)


#pdnp()
np_tst2()