from pandas import  read_excel
df=read_excel('tst.xlsx',0)
#print(df)
date=df['date']

for i in df.index:
    #print("To iterate over the list we can use a loop:",df['mandeh'][i])
	print(date[i])
