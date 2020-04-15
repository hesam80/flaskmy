from numpy import *
import numpy as np
import numpy
#numpy.loadtxt(fname, dtype=<class 'float'7gt;, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')

# Two matrices are initialized by value
x = numpy.array([[1, 2], [4, 5], [9, 10]])
y = numpy.array([[7, 8], [9, 10], [4, 5]])
#z = np.array([1, 2, 3], [8, 7], [9, 10] dtype = complex) 
#  add()is used to add matrices

print ("Addition of two matrices: " ,numpy.add(x,y))
print ("Matrix transposition : ")
print (x)
print(x.T)
for i in range(1,4):
	for j in range(7,11):
	 z=numpy.array([[i,j]])

print("z= ",z)
a = np.arange(12).reshape((3,4))
print ("a = ",a)
practice_metrice = np.array(range(12)).reshape(3,4)
print("practice_metrice is ",practice_metrice)

