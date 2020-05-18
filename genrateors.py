def genarets(i):
	while i>0 :
		yield i
		i-=1
for i in  genarets(5):
	print("?",i)
