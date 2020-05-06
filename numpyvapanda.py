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
	
def np_tst_gous():

#resource tamame inha dar

# http://www.projelecom.ir/2018/08/21/%D8%B4%D8%B1%D9%88%D8%B9-%D8%A8%D9%87-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%DA%A9%D8%AA%D8%A7%D8%A8%D8%AE%D8%A7%D9%86%D9%87-numpy-%D8%AF%D8%B1-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/ 
	X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
	D = np.sqrt(X*X+Y*Y)
	sigma, mu = 1.0, 0.0
	G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
	print(G)

def zero():
	Z = np.zeros(10)
	Z[4] = 1
	print(Z)
	d=np.eye(3)
	print(d)


#pdnp()
#np_tst2()
#np_tst_gous()
zero()