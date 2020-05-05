#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe
import numpy
import numpy as np
from pandas import  read_excel
import pandas as pd

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
print("<br>")
print("<hr>",)

def readexcl():
    df=pd.read_excel('comptst.xlsx',0)
    ind=df.index
    decprition=df['dec']
    part=df['pn']
    serof=df['snf']
    seron=df['snn']

    for i in df.index:
    #print("To iterate over the list we can use a loop:",df['mandeh'][i])
	    print(decprition[i])
	

#readexcl()