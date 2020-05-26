import stdio
import stdarray
import numpy as np
def readb():
	count = stdio.readInt()
	print(count)
	return count
def readcell():
	count = stdio.readInt()
	a=stdarray.create1D(count, False)
	for i in range(count):
		a[i]= stdio.readInt()
		print(a[i])
	return a
def readcells():
	rows = stdio.readInt()
	columns = stdio.readInt()
	a=stdarray.create2D(rows ,columns, False)
	for row in range(rows):
		for column in range(columns):
			a[row][column]=stdio.readInt()
		#	print(a[row][column])
#	print("this matric is: ", a)
	return a



def num_practice():
	z=np.zeros((5,5),dtype=int)
	z[1::2,::2]=1
	z[::2,1::2]=1
	return z

x=num_practice()
v=readcells()
z=np.array(v)
w=np.add(z,x)
print(z)
print(z.T)
print(x)
print(z.shape)
print(w)