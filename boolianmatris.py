#!C:\xampp\htdocs\pythonpro\flaskmy\env\Scripts\python.exe
#!C:\xampp\htdocs\pythonpro\flaskmy\matris.txt
import stdio
import stdarray
import numpy as np

print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("Content-Type: text/html\n charset:utf-8\n")

def readfile():
	f= open('matris.txt')
	content = f.read()
	print(content)
	return content

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
		#	print(a[row][column]) https://www.youtube.com/watch?v=Aw33ejY0BgM
#	print("this matric is: ", a)  https://www.youtube.com/channel/UCm4xezzuIlcEBFQwkAzm0CQ
	return a



def num_practice():
	z=np.zeros((5,5),dtype=int)
	z[1::2,::2]=1
	z[::2,1::2]=1
	return z

f=readfile()
print(f)
print("<hr>")
x=num_practice()
v=readcells()
z=np.array(v)
w=np.add(z,x)
print(z)
print("<br>")
print(z.T)
print("<br>")
print(x)
print("<br>")
print(z.shape)
print("<br>")
print("<hr>",)
print(w)
