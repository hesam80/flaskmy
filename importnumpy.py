#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
from numpy import *
import numpy as np
import numpy
print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("Content-Type: text/html\n charset:utf-8\n")
#numpy.loadtxt(fname, dtype=<class 'float'7gt;, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')

# Two matrices are initialized by value
x = numpy.array([[1, 2], [4, 5], [9, 10]])
y = numpy.array([[7, 8], [9, 10], [4, 5]])
#z = np.array([1, 2, 3], [8, 7], [9, 10] dtype = complex) 
#  add()is used to add matrices

print ("Addition of two matrices: " ,numpy.add(x,y))
print("<br>")

print ("Matrix transposition : ",x)

print(x.T)
print("<br>")

a = np.arange(12).reshape((3,4))
print ("a = ",a)
print("<br>")
print("<hr>")
practice_metrice = np.array(range(12)).reshape(3,4)
print("the practice_metrice is ",practice_metrice)
