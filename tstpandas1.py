import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel
'''
in codes ha az site https://pythonspot.com/read-excel-with-pandas/
estefadeh kardam
'''
df= pd.read_excel('tst.xlsx',0)

print ("columns headings:" ,df.columns)

# Using the data frame, we can get all the rows below an entire column as a list.
print(df['mandeh'])

# To iterate over the list we can use a loop:
for i in df.index:
    print("To iterate over the list we can use a loop:",df['mandeh'][i])

# can save an entire column into a list:
listdate=df['date']
print("save an entire column into a list listdate[0] is ",listdate[0])

# ake entire columns from an excel sheet
date=df['date']
mandeh = df['mandeh']
bestankar=df['bestankar']
bedehkar=df['bedehkar']
print("mandeh\n",df['mandeh'])
