#!C:\Users\921404\AppData\Local\Programs\Python\Python38-32\python.exe


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import stdio
print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("Content-Type: text/html\n charset:utf-8\n")
print("<br><B>hello python</B>")
df = pd.read_excel('tst.xlsx', sheetname='Sheet1')

print("Column headings:")
print(df.columns)

