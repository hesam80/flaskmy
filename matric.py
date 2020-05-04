import numpy as np
from pandas import  read_excel

def matric():
   c=np.empty(8)
   print('matris c= ',c)
   d = np.empty([2, 2], dtype=int)
   print("matris d=", d)
   f=np.arange(5)
   print("matris f=", f)

def tahlil():

   df=read_excel('comptst.xlsx',0)
   ind=df.index
   decprition=df['dec']
   part=df['pn']
   serof=df['snf']
   seron=df['snn']
   #integrate=df['snf'].mean()
   print(df.head())
   #print("majmoo is:", integrate)

tahlil()