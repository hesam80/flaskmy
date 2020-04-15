from pandas import  read_excel
df=read_excel('tst.xlsx',0)
print(df)
for index in df.itetrows():
	print(index)
	
