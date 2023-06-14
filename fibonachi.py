import sys
import stdio
print("javaabe addade count : ")
def fibonachi(n):
	a=0
	b=1
	print("series fibonachi",n,"is = ",end='')
	while a<n:
		print(a , end='')
		
		a, b = b, a+b
	print()
count = stdio.readInt()
fibonachi(count)

