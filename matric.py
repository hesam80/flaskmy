import numpy as np
from pandas import  read_excel
import random
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

def zoj(n):
   num = random.randint(1,int(n))
   for num in range(num):
      if num % 2 == 0 :
        print("found a zoj number :" , num)
        continue
      print("fard number: ",num)



zoj(13.15)
#tahlil()
