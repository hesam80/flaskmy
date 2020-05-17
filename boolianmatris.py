import stdio
import stdarray
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
	print("this matric is: ", a)
	return a

readcells()